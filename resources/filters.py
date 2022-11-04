from lock import lock
from flask_restful import Resource, reqparse
from http import HTTPStatus

from models.products import ProductsModel, categories_list, condition_list


class Filter(Resource):

    # retrieve products by filters applied
    def post(self):
        with lock.lock:
            data = self.get_data()

            # in case the price is reversed for some reason...
            price0 = data['price0']
            price1 = data['price1']
            category = data['category']
            conditions = data['conditions']
            date = data['date']

            not_valid = (category is not None and category not in categories_list) or\
                        (price0 < 0 or price1 < 0 or price0 is None or price1 is None) or\
                        not set(conditions).issubset(condition_list) or \
                        date is None
            price0 = min(price0, price1)
            price1 = max(price0, price1)

            # check if everything is valid
            if not_valid:
                return {'message': "One of the filters are not correct".format(data)}, \
                       HTTPStatus.BAD_REQUEST
            # if everything is ok then return the products, if nothing matches, return empty list
            products = ProductsModel.get_by_filters(category, price0, price1, date, conditions)
            products = [x.json() for x in products] if products else []
            return {"products_list": products}, HTTPStatus.OK

    def get_data(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type
        parser.add_argument('category', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('price0', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('price1', type=int, required=True, help="This field cannot be left blank")
        parser.add_argument('conditions', type=str, action='append', required=True,
                            help="This field cannot be left blank")
        parser.add_argument('date', type=int, required=True, help="This field cannot be left blank")

        return parser.parse_args()


class FilterCategory(Resource):

    # retrieve products by category
    def get(self, category):
        with lock.lock:
            not_valid = category is None or category not in categories_list

            # check if everything is valid
            if not_valid:
                return {'message': "Invalid cateogry".format(category)}, \
                       HTTPStatus.BAD_REQUEST
            # if everything is ok then return the products, if nothing matches, return empty list
            products = ProductsModel.get_by_category(category)
            products = [x.json() for x in products] if products else []
            return {"products_list": products}, HTTPStatus.OK
