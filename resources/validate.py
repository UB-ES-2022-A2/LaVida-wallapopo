import datetime
from http import HTTPStatus

from flask_restful import Resource, reqparse
from itsdangerous import URLSafeTimedSerializer

from db import db
from lock import lock
from models.accounts import AccountsModel


class Validate(Resource):

    def get(self):
        return self

    def post(self):
        print("Validate post: ", self)
        data = self.get_data()
        print("data: ", data)
        token = data['validation_token']
        print("post token: ", token)

        with lock.lock:
            print("Confirm_email")
            email = ''
            try:
                # email = self.confirm_token(token)
                from app import app
                serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
                try:
                    email = serializer.loads(
                        token,
                        salt=app.config['SECURITY_PASSWORD_SALT'],
                        max_age=3600
                    )
                except:
                    print("Token is not valid!")
                    return None
                print("Token is valid!")
            except Exception as e:
                print(e)
                return None

            user = AccountsModel.get_by_email(email)
            if user.confirmed:
                print("Account already confirmed!")
                return {'message': "Account already confirmed, please login"}, HTTPStatus.CONFLICT
            else:
                user.confirmed = True
                user.confirmed_on = datetime.datetime.now()
                db.session.add(user)
                db.session.commit()
                print("Account confirmed!")
                return {'message': "Account email confirmed!"}, HTTPStatus.OK


    def get_data(self):
        parser = reqparse.RequestParser()  # create parameters parser from request
        parser.add_argument('validation_token', type=str, required=True, help="This field cannot be left blank")
        return parser.parse_args()
