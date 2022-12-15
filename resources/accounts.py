import datetime
from http import HTTPStatus

from flask_restful import Resource, reqparse
from itsdangerous import URLSafeTimedSerializer
from sqlalchemy import exc

from db import db
from lock import lock
from models.accounts import AccountsModel, auth, g, EMAIL_REGEX, PASSWORD_REGEX

import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'wallapopo.confirmation@gmail.com'
EMAIL_PASSWORD = 'cgklydfzsujtprcs'


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
                return {'message': 'Email [{}] is not a valid format'.format(data['email'])}, \
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
            new_account = AccountsModel(email=data['email'], username=data['username'], confirmed=False)
            # assign the hashed password to the user
            new_account.hash_password(data['password'])

            # Generació del token de confirmacio de correu
            email_token = self.generate_confirmation_token(data['email'])
            print("confirmation token is: {}".format(email_token))

            # confirm_url2 = flask.url_for('confirm', token=email_token, _external=True)
            # print("URL2: ", confirm_url2)
            # TODO: cambiar para coger url en funcion del entorno (local o cloud)
            # 8080 for dev
            # export const devWeb = 'http://127.0.0.1:5000/'
            # export const prodWeb = 'https://firm-affinity-366616.ew.r.appspot.com/'
            confirm_url = "https://wallapopo-ub.ew.r.appspot.com/#/emailConfirmation/validation_token=" + email_token

            msg = EmailMessage()
            msg['Subject'] = 'Test python email'
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = data['email']

            html_message = '''
                            <p>Por favor, sigue este link para activar tu cuenta:</p>
                            <p><a href="{{confirm_url}}">{{confirm_url}}</a></p>
                            <br>
                            <p>Un saludo!</p>
                            '''
            html_message = html_message.replace('{{confirm_url}}', confirm_url)

            msg.set_content(
                html_message,
                subtype='html')

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)

            # update DB
            try:
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

    # Genera un nou token de confirmacio
    def generate_confirmation_token(self, email):
        from app import app
        serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])

    def confirm_email(self, token):
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
            return {'message': "Account already confirmed, please login"}, HTTPStatus.CONFLICT
        else:
            user.confirmed = True
            user.confirmed_on = datetime.datetime.now()
            db.session.add(user)
            db.session.commit()
            return {'message': "Account email confirmed!"}, HTTPStatus.OK

