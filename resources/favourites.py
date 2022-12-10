from lock import lock
from flask_restful import Resource, reqparse
from http import HTTPStatus
from sqlalchemy import exc

from db import db
from models.favourites import FavouritesModel
from models.accounts import auth, AccountsModel, g


class Favourite(Resource):

    # return product by id
    def get(self, id):
        favourite = FavouritesModel.get_by_id(id)
        if favourite is None:
            return {"message": "Favourite product with ID [{}] does not exist".format(id)}, HTTPStatus.NOT_FOUND
        return {"favourite_product": favourite.json()}, HTTPStatus.OK


class FavouritesList(Resource):

    def get(self):
        favourites = FavouritesModel.get_products_by_fav()
        return {
            "Favourites_list": [x.json() for x in favourites]}, HTTPStatus.OK if favourites else HTTPStatus.NOT_FOUND


class AddFavourite(Resource):

    # add new favourite
    @auth.login_required()
    def post(self, email):
        with lock.lock:
            data = self.get_data()

            account = AccountsModel.get_by_email(email)
            if account is None:  # return error message if order doesn't exist
                return {'message': 'This email [{}] does not exist'.format(email)}, HTTPStatus.NOT_FOUND
            # return error if the account username doesn't match
            if account.username != g.user.username:
                return {'message': "Bad authorization user"}, HTTPStatus.BAD_REQUEST

            # add product to DB
            try:
                new_favourite = FavouritesModel(name=data['name'],
                                                liked=data['liked'],
                                                )
                new_favourite.user_id = account.email
                new_favourite.save_to_db()
                return new_favourite.json(), HTTPStatus.OK
            except exc.SQLAlchemyError:
                db.session.rollback()  # rollback in case something went wrong
                return {'message': 'Error while adding new favourite'}, HTTPStatus.INTERNAL_SERVER_ERROR

    def get_data(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type
        parser.add_argument("name", type=str, required=True, help="This field cannot be left blank")
        parser.add_argument("liked", type=bool, required=True, help="This field cannot be left blank")

        return parser.parse_args()
