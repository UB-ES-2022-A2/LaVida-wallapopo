from lock import lock
from flask_restful import Resource, reqparse
from http import HTTPStatus
from sqlalchemy import exc
import datetime

from models.accounts import *
from models.favourites import FavouritesModel
from models.products import ProductsModel


class Favourites(Resource):

    @auth.login_required()
    def get(self, email):
        with lock.lock:
            account = AccountsModel.get_by_email(email)
            # return account if it exists
            if account is None:  # return error message if order doesn't exist
                return {'message': 'account with email [{}] does not exist'.format(email)}, HTTPStatus.NOT_FOUND
            # return error if the account email doesn't match
            if account.username != g.user.username:
                return {'message': "Bad authorization user"}, HTTPStatus.BAD_REQUEST

            favourites = FavouritesModel.get_by_email(email)
            # return favourites if it exists
            return {"favourites_list": [x.json() for x in favourites]}, HTTPStatus.OK

    @auth.login_required()
    def post(self):
        with lock.lock:
            # get the arguments
            data = self.get_data()

            account = AccountsModel.get_by_email(data['email'])
            product = ProductsModel.get_by_id(data['product_id'])
            # return error if account doesn't exist
            if account is None:
                return {'message': "account with email [{}] does not exist".format(data['email'])}, HTTPStatus.CONFLICT

            # return error if the account username doesn't match
            if account.username != g.user.username:
                return {'message': "Bad authorization user"}, HTTPStatus.BAD_REQUEST

            # return error if product does not exist
            if product is None:
                return {'message': "product with id [{}] doesn't exist".format(data['product_id'])}, HTTPStatus.CONFLICT

            fav = FavouritesModel.get_fav(data['email'], data['product_id'])

            if fav:
                return {'message': "product with id [{}] is already in your favourite list".
                        format(data['product_id'])}, HTTPStatus.CONFLICT

            # add new favourite to db
            try:
                new_favourite = FavouritesModel(
                    data['email'],
                    data['product_id']
                )
                new_favourite.save_to_db()
                return new_favourite.json(), HTTPStatus.OK
            except exc.SQLAlchemyError:
                db.session.rollback()  # rollback in case something went wrong
                return {'message': 'error while adding product to favourites'}, HTTPStatus.INTERNAL_SERVER_ERROR

    @auth.login_required()
    def delete(self):
        with lock.lock:
            # get the arguments
            data = self.get_data()

            account = AccountsModel.get_by_email(data['email'])
            product = ProductsModel.get_by_id(data['product_id'])
            # return error if account doesn't exist
            if account is None:
                return {'message': "account with email [{}] does not exist".format(data['email'])}, HTTPStatus.CONFLICT

            #return error if the account username doesn't match
            #if account.username != g.user.username:
            #return {'message': "Bad authorization user"}, HTTPStatus.BAD_REQUEST

            # return error if product does not exist
            if product is None:
                return {'message': "product with id [{}] doesn't exist".format(data['product_id'])}, HTTPStatus.CONFLICT

            fav = FavouritesModel.get_fav(data['email'], data['product_id'])

            if not fav:
                return {'message': "product with id [{}] is not in your favourites list".
                        format(data['product_id'], data['email'])}, HTTPStatus.CONFLICT

            # delete fav from user
            try:
                fav.delete_from_db()
                return {'message': 'product with id [{}] deleted from favourites'.format(data['product_id'])}, HTTPStatus.OK
            except exc.SQLAlchemyError:
                db.session.rollback()  # rollback in case something went wrong
                return {'message': 'error while deleting product to favourites'}, HTTPStatus.INTERNAL_SERVER_ERROR

    def get_data(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('product_id', type=int, required=True, help="This field cannot be left blank")

        return parser.parse_args()
