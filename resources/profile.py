from http import HTTPStatus
from flask_restful import Resource, reqparse

from db import db
from models.accounts import AccountsModel, auth, g


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

    def post(self):
        data = self.get_data()
        email = data['email']
        user = AccountsModel.get_by_email(email)
        # return error message if account doesn't exist
        if user is None:
            return {'message': 'This email [{}] does not exist'.format(email)}, HTTPStatus.NOT_FOUND

        try:
            user.profile_picture = data['image']
            user.name = data['name']
            user.surname = data['surname']
            # user.location = data['location']

            db.session.add(user)
            db.session.commit()

        except Exception as e:
            print(e)
            return {'message': "Error updating the profile"}, HTTPStatus.INTERNAL_SERVER_ERROR

        return {'message': "Profile updated successfully"}, HTTPStatus.OK

    def get_data(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('image', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument("name", type=str, required=True, help="This field cannot be left blank")
        parser.add_argument("surname", type=str, required=True, help="This field cannot be left blank")
        # parser.add_argument("location", type=str, required=True, help="This field cannot be left blank")

        return parser.parse_args()

