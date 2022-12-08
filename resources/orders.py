from lock import lock
from flask_restful import Resource, reqparse
from http import HTTPStatus
from sqlalchemy import exc
import datetime

from models.accounts import *
from models.orders import OrdersModel
from models.products import ProductsModel


class Orders(Resource):

    @auth.login_required()
    def post(self, email):
        with lock.lock:
            # get the arguments
            data = self.get_data()

            account = AccountsModel.get_by_email(email)
            product = ProductsModel.get_by_id(data['product_id'])
            # return error if account doesn't exist
            if account is None:
                return {'message': "account with email [{}] does not exist".format(email)}, HTTPStatus.CONFLICT

            # return error if the account username doesn't match
            if account.username != g.user.username:
                return {'message': "Bad authorization user"}, HTTPStatus.BAD_REQUEST

            # return error if product does not exist
            if product is None:
                return {'message': "match with id [{}] doesn't exist".format(data['match_id'])}, HTTPStatus.CONFLICT

            # add new order to db
            try:
                cc_exp_date = '1/' + data['cc_exp_date']
                cc_exp_date = cc_exp_date.split('/')
                cc_exp_date.reverse()
                new_order = OrdersModel(
                    email,
                    product.user_id,
                    product.id,
                    data['credit_card'],
                    data['cvc'],
                    data['cc_owner'],
                    datetime.date(*map(int, cc_exp_date))
                )
                product.status = 'Vendido'
                new_order.save_to_db()
                return new_order.json(), HTTPStatus.OK
            except exc.SQLAlchemyError:
                db.session.rollback()  # rollback in case something went wrong
                return {'message': 'error while creating new order'}, HTTPStatus.INTERNAL_SERVER_ERROR

    def get_data(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type
        parser.add_argument('product_id', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('credit_card', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('cvc', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('cc_exp_date', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('cc_owner', type=str, required=True, help="This field cannot be left blank")

        return parser.parse_args()


class Sales(Resource):

    @auth.login_required()
    def get(self, email):
        account = AccountsModel.get_by_email(email)
        # return account if it exists
        if account is None:  # return error message if order doesn't exist
            return {'message': 'This email [{}] does not exist'.format(email)}, HTTPStatus.NOT_FOUND
        # return error if the account email doesn't match
        if account.username != g.user.username:
            return {'message': "Bad authorization user"}, HTTPStatus.BAD_REQUEST

        orders = OrdersModel.get_sales_by_email(email)
        # return orders if it exists
        return {"orders_list": [x.json() for x in orders]}, HTTPStatus.OK


class Purchases(Resource):

    @auth.login_required()
    def get(self, email):
        account = AccountsModel.get_by_email(email)
        # return account if it exists
        if account is None:  # return error message if order doesn't exist
            return {'message': 'This email [{}] does not exist'.format(email)}, HTTPStatus.NOT_FOUND
        # return error if the account email doesn't match
        if account.username != g.user.username:
            return {'message': "Bad authorization user"}, HTTPStatus.BAD_REQUEST

        orders = OrdersModel.get_purchases_by_email(email)
        # return orders if it exists
        return {"orders_list": [x.json() for x in orders]}, HTTPStatus.OK
