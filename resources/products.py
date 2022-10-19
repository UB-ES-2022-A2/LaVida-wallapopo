from lock import lock
from flask_restful import Resource, reqparse
from http import HTTPStatus
from sqlalchemy import exc

from db import db
from models.products import ProductsModel
from models.accounts import auth, AccountsModel, g


class ProductsList(Resource):

    # return all products
    def get(self):
        products = ProductsModel.get_all()
        return {"Products List": [x.json() for x in products]}, HTTPStatus.OK if products else HTTPStatus.NOT_FOUND

