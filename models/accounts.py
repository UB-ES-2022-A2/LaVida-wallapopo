import time
from db import db, secret_key
from passlib.apps import custom_app_context as pwd_context
from jwt import encode, decode, ExpiredSignatureError, InvalidSignatureError
from flask_httpauth import HTTPBasicAuth
from flask import g, current_app

auth = HTTPBasicAuth()


class AccountsModel(db.Model):
    __tablename__ = 'accounts'

    # info needed for login
    email = db.Column(db.String(), primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    # optional account details
    name = db.Column(db.String(20), nullable=True)
    surname = db.Column(db.String(30), nullable=True)
    birthday = db.Column(db.DateTime(), nullable=True)
    profile_picture = db.Column(db.String(), nullable=True)  # can be stored as url
    # 0 not admin/ 1 is admin
    is_admin = db.Column(db.Integer, nullable=False)
    # products db not created yet
    # products = db.relationship('ProductsModel', backref='products', lazy=True)

    def __init__(self, email, is_admin=0):
        self.email = email
        self.is_admin = is_admin

    def json(self):
        return {'email': self.email,
                'name': self.username,
                'surname': self.surname,
                'birthday': self.birthday,
                'is_admin': self.is_admin
                }

    def generate_auth_token(self, expiration=600):
        return encode(
            {"email": self.email, "exp": int(time.time()) + expiration},
            current_app.secret_key,
            algorithm="HS256"
        )

    @classmethod
    def verify_auth_token(cls, token):
        try:
            data = decode(token, secret_key, algorithms=["HS256"])
        except ExpiredSignatureError:
            return None  # expired token
        except InvalidSignatureError:
            return None  # invalid token

        user = cls.query.filter_by(email=data['email']).first()

        return user

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):  # returns all accounts
        return cls.query.all()

    @classmethod
    def get_by_email(cls, email):
        return cls.query.get(email)

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password_(self, password):
        return pwd_context.verify(password, self.password)

    @auth.verify_password
    def verify_password(token, password):
        g.user = AccountsModel.verify_auth_token(token)
        return g.user

    @auth.get_user_roles
    def get_user_roles(user):
        return ['admin'] if user.is_admin else ['user']