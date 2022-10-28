from lock import lock
from flask_restful import Resource, reqparse
from http import HTTPStatus
from sqlalchemy import exc

from db import db
from models.accounts import AccountsModel, auth, g, EMAIL_REGEX, PASSWORD_REGEX


class Accounts(Resource):

    @auth.login_required()
    def get(self, email):
        account = AccountsModel.get_by_email(email)
        # return account if it exists
        if account is None:  # return error message if order doesn't exist
            return {'message': 'This email [{}] does not exist'.format(email)}, HTTPStatus.NOT_FOUND
        # return error if the account email doesn't match
        if account.username != g.user.username:
            return {'message': "Bad authorization user"}, HTTPStatus.BAD_REQUEST

        return {'account': account.json()}, HTTPStatus.OK

    # register new accounts
    def post(self):
        with lock.lock:
            data = self.get_data()
            # Check if the email has a valid email format
            if EMAIL_REGEX.match(data['email']) is None:
                return {'Email [{}] is not a valid format'.format(data['email'])}, \
                       HTTPStatus.BAD_REQUEST
            account = AccountsModel.get_by_email(data['email'])
            account2 = AccountsModel.get_by_username(data['username'])

            # return error if account already exist
            if account is not None:
                return {'message': "Account with email [{}] already exist".format(data['email'])}, \
                       HTTPStatus.CONFLICT
            if account2 is not None:
                return {'message': "Username [{}] is already in use".format(data['username'])}, \
                       HTTPStatus.CONFLICT
            # minimum eight characters, at least one letter, one number and one special character
            if PASSWORD_REGEX.match(data['password']) is None:
                return {'message': "Password is necessary to register"}, HTTPStatus.CONFLICT

            # create new account
            new_account = AccountsModel(email=data['email'], username=data['username'])
            # assign the hashed password to the user
            new_account.hash_password(data['password'])
            # update DB
            try:
                print(new_account.password)
                new_account.save_to_db()
                return new_account.json(), HTTPStatus.OK
            except exc.SQLAlchemyError:
                db.session.rollback()  # rollback in case something went wrong
                return {'message': 'Error while creating new account'}, HTTPStatus.INTERNAL_SERVER_ERROR

    def get_data(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type
        parser.add_argument('email', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('username', type=str, required=True, help="This field cannot be left blank")
        parser.add_argument('password', type=str, required=True, help="This field cannot be left blank")

        return parser.parse_args()
