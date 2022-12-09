import datetime

import pytest

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api
from config import config
from resources.accounts import Accounts
from resources.products import Product, ProductsList, AddProduct
from resources.profile import Profile
from resources.orders import Orders, Sales, Purchases
from resources.session import Login, Logout
from resources.filters import Filter, FilterCategory
from resources.validate import Validate
from resources.reviews import Reviews
from db import db
import random as rand
from sqlalchemy import exc
import resources.sample_data as data

from requests.auth import HTTPBasicAuth
from models.accounts import AccountsModel
from models.products import ProductsModel
from models.orders import OrdersModel


def populate_db():
    products = []
    accounts = []

    for product in data.products:
        new_product = ProductsModel(name=product['name'], category=product['category'],
                                    description=product['description'], price=product['price'],
                                    condition=product['condition'])

        new_product.image = product['image']
        products.append(new_product)

    for account in data.accounts:
        new_account = AccountsModel(email=account['email'], username=account['username'],
                                    confirmed=account['confirmed'])

        new_account.hash_password(account['password'])
        accounts.append(new_account)

    # Relationship between products and user
    for product in products:
        user = rand.choice(accounts)
        i = accounts.index(user)
        product.user_id = accounts[i].email

    try:
        db.session.add_all(products)
        db.session.add_all(accounts)
        db.session.commit()
    except exc.SQLAlchemyError:
        db.session.rollback()


def create_app():
    app = Flask(__name__)

    environment = config['testing']

    app.config.from_object(environment)
    app.config['SECURITY_PASSWORD_SALT'] = 'foobar'

    # from db import db
    db = SQLAlchemy()
    migrate = Migrate(app, db)
    db.init_app(app)

    api = Api(app)
    CORS(app, resources={r'/*': {'origins': '*'}})

    api.add_resource(Accounts, '/API/account/<string:email>', '/API/account')
    api.add_resource(Validate, '/API/validation/<string:validation_token>', '/API/validation')
    api.add_resource(Profile, '/API/profile/<string:email>', '/API/profile')
    api.add_resource(Reviews, '/API/reviews/<string:email>', '/API/reviews')

    # products
    api.add_resource(Product, '/API/product/<string:id>')
    api.add_resource(ProductsList, '/API/products')
    api.add_resource(AddProduct, '/API/catalog/add/<string:email>')

    # filtering
    api.add_resource(Filter, '/API/filter')
    api.add_resource(FilterCategory, '/API/filter/<string:category>')

    # session
    api.add_resource(Login, '/API/login')
    api.add_resource(Logout, '/API/logout/<string:email>')

    # orders
    api.add_resource(Orders, '/API/order/add/<string:email>')
    api.add_resource(Purchases, '/API/order/purchases/<string:email>')
    api.add_resource(Sales, '/API/order/sales/<string:email>')

    return app

# --------
# Fixtures
# --------
@pytest.fixture()
def _app():
    app = create_app()
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()
        populate_db()
        yield app
        db.drop_all()


@pytest.fixture()
def client(_app):
    return _app.test_client()


@pytest.fixture()
def auth_header(client):
    import base64

    json = {'email': 'pepe432@gmail.com', 'password': 'pepe123,.'}
    login = client.post("API/login", json=json)
    token = login.json
    headers = {
        'Authorization': 'Basic {}'.format(
            base64.b64encode(
                '{token}:{password}'.format(
                    token=token['token'],
                    password='').encode()
            ).decode()
        )
    }
    yield headers


@pytest.fixture(scope='function')
def first_product(client):
    product = client.get("http://localhost:5000/API/product/1")
    return product.json


@pytest.fixture(scope='function')
def dummy_user():
    acc = AccountsModel("dummy@gmail.com", "dummyname", False)
    acc.password = "qwerty12."
    return acc


@pytest.fixture(scope='function')
def dummy_password(dummy_user):
    dummy_user.hash_password(dummy_user.password)
    return dummy_user.password


@pytest.fixture(scope='function')
def switch_product():
    p = ProductsModel("Nintendo Switch", "Consolas y Videojuegos", "Apenas la uso y necesito dinero", 150, "Casi nuevo")
    p.id = 99
    p.user_id = "pepe432@gmail.com"
    return p


@pytest.fixture(scope='function')
def pepe_products(_app):
    with _app.app_context():
        p = ProductsModel.get_all_by_user("pepe432@gmail.com")
        return p


@pytest.fixture(scope='function')
def user_auth(_app, client):
    json = {'email': 'pepe432@gmail.com', 'password': 'pepe123,.'}
    with _app.test_request_context():
        login = client.post("API/login", data=json)
        token = login.json
        auth = HTTPBasicAuth(token['token'], '')
        return auth


@pytest.fixture(scope='function')
def products_json(client):
    products = client.get("API/products")
    return products.json


@pytest.fixture()
def gmail_imap():
    import imaplib
    # account credentials
    username = "wallapopodummy@gmail.com"
    password = "uzrvtptxessitpfi"
    # Gmail provider's IMAP server (from https://www.systoolsgroup.com/imap/)
    imap_server = "imap.gmail.com"
    # Create an IMAP4 class with SSL
    imap = imaplib.IMAP4_SSL(imap_server, 993)
    # Authenticate
    imap.login(username, password)

    yield imap

    imap.close()
    imap.logout()
