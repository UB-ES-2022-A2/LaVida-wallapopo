from lock import lock
from http import HTTPStatus
from flask_restful import Resource, reqparse
from models.accounts import AccountsModel, EMAIL_REGEX


class Login(Resource):
    def post(self):
        with lock.lock:
            data = self.get_data()

            # Check if the email has a valid email format
            if EMAIL_REGEX.match(data['email']) is None:
                return {'message': "Email [{}] is not a valid format".format(data['email'])}, \
                       HTTPStatus.BAD_REQUEST
            account = AccountsModel.get_by_email(data['email'])  # find the matching account

            # return error if account doesn't exist
            if account is None:
                return {'message': "Account with email [{}] does not exist".format(data['email'])}, \
                       HTTPStatus.NOT_FOUND
            # return error if account doesn't exist
            if (data['password']) is None:
                return {'message': "Password can not be blank".format(data['email'])}, \
                       HTTPStatus.CONFLICT
            # return error if password doesn't match with username
            if not account.verify_password_(data['password']):
                return {'message': "Email or Password are incorrect"}, HTTPStatus.BAD_REQUEST

            # generate token with a time limit of 10 minutes
            token = account.generate_auth_token()
            return {'token': token.decode('ascii')}, 200

    def get_data(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('password', type=str, required=True, help="This field cannot be left blank")

        return parser.parse_args()

