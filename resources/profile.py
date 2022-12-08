from http import HTTPStatus
from flask_restful import Resource, reqparse

from db import db
from models.accounts import AccountsModel, auth, g

import datetime

class Profile(Resource):

    @auth.login_required()
    def get(self, email):
        account = AccountsModel.get_by_email(email)
        # return account if it exists
        if account is None:  # return error message if order doesn't exist
            return {'message': 'This email [{}] does not exist'.format(email)}, HTTPStatus.NOT_FOUND

        # return error if the account email doesn't match
        if account.username != g.user.username:
            return {'message': "Bad authorization user"}, HTTPStatus.UNAUTHORIZED

        return {'account': account.json()}, HTTPStatus.OK


    @auth.login_required
    def put(self, email):
        data = self.get_data()
        for i in data:
            print(i)
        user = AccountsModel.get_by_email(email)
        # return error message if account doesn't exist
        if user is None:
            return {'message': 'This email [{}] does not exist'.format(email)}, HTTPStatus.NOT_FOUND
        if user.username != g.user.username:
            return {'message': "Bad authorization user"}, HTTPStatus.UNAUTHORIZED
        if data["name"]:
            user.name = data["name"]
        if data["surname"]:
            user.surname = data["surname"]
        if data["birthday"]:
            user.birthday = datetime.date(*map(int, data["birthday"].split('-')))
            print(user.birthday)

        db.session.add(user)
        db.session.commit()
        user = AccountsModel.get_by_email(email)
        print(user.json())
        return {'message': "Profile updated successfully"}, HTTPStatus.OK

    def get_data(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('image', type=str, required=False, help="This field cannot be left blank")
        parser.add_argument("name", type=str, required=False, help="This field cannot be left blank")
        parser.add_argument("surname", type=str, required=False, help="This field cannot be left blank")
        parser.add_argument("birthday", type=str, required=False, help="This field cannot be left blank")
        # parser.add_argument("location", type=str, required=True, help="This field cannot be left blank")

        return parser.parse_args()

