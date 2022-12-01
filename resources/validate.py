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
        data = self.get_data()
        token = data['validation_token']
        with lock.lock:
            print("Confirming email token")
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
                    return {'message': "El link de verificación no es correcto"}, HTTPStatus.CONFLICT
                print("Token is valid!")
            except Exception as e:
                print(e)
                return {'message': "No hemos podido verificar la cuenta. Si el error persiste contacta con los "
                                   "desarroladores"}, HTTPStatus.INTERNAL_SERVER_ERROR

            user = AccountsModel.get_by_email(email)
            if user.confirmed:
                print("Account already confirmed!")
                return {'message': "Tu cuenta ya estaba verificada. Puedes iniciar sesión."}, HTTPStatus.OK

            else:
                user.confirmed = True
                user.confirmed_on = datetime.datetime.now()
                db.session.add(user)
                db.session.commit()
                print("Account confirmed!")
                return {'message': "Cuenta verificada correctamente! Puedes iniciar sesión."}, HTTPStatus.OK

    @staticmethod
    def get_data():
        parser = reqparse.RequestParser()  # create parameters parser from request
        parser.add_argument('validation_token', type=str, required=True, help="This field cannot be left blank")
        return parser.parse_args()
