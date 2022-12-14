from lock import lock
from flask_restful import Resource, reqparse
from http import HTTPStatus
from sqlalchemy import exc
import datetime

from models.accounts import *
from models.reviews import ReviewsModel
from models.products import ProductsModel
from models.orders import OrdersModel


class Reviews(Resource):

    @auth.login_required()
    def get(self, email):
        account = AccountsModel.get_by_email(email)
        # return account if it exists
        if account is None:  # return error message if order doesn't exist
            return {'message': 'account with email [{}] does not exist'.format(email)}, HTTPStatus.NOT_FOUND
        # return error if the account email doesn't match
        if account.username != g.user.username:
            return {'message': "Bad authorization user"}, HTTPStatus.BAD_REQUEST

        reviews = ReviewsModel.get_reviews_by_email(email)
        # return orders if it exists
        return {"reviews_list": [x.json() for x in reviews]}, HTTPStatus.OK

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

            orders = OrdersModel.get_purchases_by_email(data['email'])
            order = next((o for o in orders if o.buyer_id == data['email'] and o.product_id == product.id), None)
            # return error if the user hasn't purchased this product
            if order is None:
                return {'message': "user with email [{}] hasn't purchased product with id [{}]".format(
                    data['email'], product.id)}, HTTPStatus.CONFLICT

            # add new review to db
            try:
                new_review = ReviewsModel(
                    data['email'],
                    order.seller_id,
                    product.id,
                    data['stars'],
                    data['comment']
                )

                new_review.save_to_db()
                order.reviewed = True
                order.save_to_db()
                return new_review.json(), HTTPStatus.OK
            except exc.SQLAlchemyError:
                db.session.rollback()  # rollback in case something went wrong
                return {'message': 'error while saving new review'}, HTTPStatus.INTERNAL_SERVER_ERROR

    @auth.login_required
    def put(self, id):
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

            orders = OrdersModel.get_all()
            order = next((o for o in orders if o.product_id == id), None)
            # if order exists, update the reviewed status
            if order is None:
                return {'message': "this order doesn't exist"}, HTTPStatus.CONFLICT
            order.reviewed = True

            # get review by id and update its fields
            reviews = ReviewsModel.get_all()
            review = next((r for r in reviews if r.product_id == id), None)
            if review is None:
                return {'message': "this review doesn't exist"}, HTTPStatus.CONFLICT

            if data["stars"]:
                review.stars = data["stars"]
            if data["comment"]:
                review.comment = data["comment"]

            try:
                db.session.add(review)
                db.session.add(order)
                db.session.commit()
                return {'message': "Review updated successfully"}, HTTPStatus.OK
            except exc.SQLAlchemyError:
                db.session.rollback()  # rollback in case something went wrong
                return {'message': 'Error while modifying review information'}, HTTPStatus.INTERNAL_SERVER_ERROR

    def get_data(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('product_id', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('stars', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('comment', type=str, required=True, help="This field cannot be left blank")

        return parser.parse_args()

