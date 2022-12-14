from lock import lock
from http import HTTPStatus
from flask_restful import Resource, reqparse
from models.accounts import AccountsModel, auth, g, EMAIL_REGEX, PASSWORD_REGEX


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
            # return error if password doesn't match with email
            if not account.verify_password_(data['password']):
                return {'message': "Email or Password are incorrect"}, HTTPStatus.BAD_REQUEST

            # generate token with a time limit of 10 minutes
            token = account.generate_auth_token()
            return {'token': token}, 200

    def get_data(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('password', type=str, required=True, help="This field cannot be left blank")

        return parser.parse_args()


class Logout(Resource):

    @auth.login_required()
    def post(self, email):
        account = AccountsModel.get_by_email(email)
        # return account if it exists
        if account is None:  # return error message if order doesn't exist
            return {'message': 'This email [{}] does not exist'.format(email)}, HTTPStatus.NOT_FOUND
        # return error if the account email doesn't match
        if account.username != g.user.username:
            return {'message': "Bad authorization user"}, HTTPStatus.BAD_REQUEST
        account.invalidate_auth_token()

        return {'message': 'Logged out'}, HTTPStatus.OK
