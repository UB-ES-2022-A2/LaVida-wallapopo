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

