from lock import lock
from flask_restful import Resource, reqparse
from http import HTTPStatus
from sqlalchemy import exc

from db import db
from models.products import ProductsModel
from models.accounts import auth, AccountsModel, g


class Product(Resource):

    # return product by id
    def get(self, id):
        product = ProductsModel.get_by_id(id)
        return {"product": product.json()}, HTTPStatus.OK if product else HTTPStatus.NOT_FOUND


class ProductsList(Resource):

    # return all products
    def get(self):
        products = ProductsModel.get_all()
        return {"Products_List": [x.json() for x in products]}, HTTPStatus.OK if products else HTTPStatus.NOT_FOUND


class AddProduct(Resource):

    # add new products
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
                new_product = ProductsModel(name=data['name'],
                                            category=data['category'],
                                            description=data['description'],
                                            price=data['price'],
                                            condition=data['condition']
                                            )
                new_product.shipment = data['shipment']
                new_product.user_id = account.email
                new_product.save_to_db()
                return new_product.json(), HTTPStatus.OK
            except exc.SQLAlchemyError:
                db.session.rollback()  # rollback in case something went wrong
                return {'message': 'Error while adding new product'}, HTTPStatus.INTERNAL_SERVER_ERROR

    def get_data(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type
        parser.add_argument('name', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument("category", type=str, required=True, help="This field cannot be left blank")
        parser.add_argument("price", type=float, required=True, help="This field cannot be left blank")
        parser.add_argument("condition", type=str, required=True, help="This field cannot be left blank")
        parser.add_argument("description", type=str, required=True, help="This field cannot be left blank")
        parser.add_argument("shipment", type=bool, required=True, help="This field cannot be left blank")
        # TODO add images

        return parser.parse_args()
