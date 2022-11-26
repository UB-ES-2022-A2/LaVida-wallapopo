from http import HTTPStatus
from flask_restful import Resource
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
            return {'message': "Bad authorization user"}, HTTPStatus.BAD_REQUEST

        return {'account': account.json()}, HTTPStatus.OK
