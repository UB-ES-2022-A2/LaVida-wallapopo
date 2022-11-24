import pytest

import requests
from app import app
from db import db
import random as rand
from sqlalchemy import exc
import resources.sample_data as data

from requests.auth import HTTPBasicAuth
from models.accounts import AccountsModel
from models.products import ProductsModel


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


# --------
# Fixtures
# --------
@pytest.fixture()
def _app():
    with app.app_context():
        db.create_all()
        populate_db()
        yield app
        db.drop_all()


@pytest.fixture()
def client(_app):
    from app import app
    return app.test_client()


@pytest.fixture(scope='function')
def first_product():
    product = requests.get("http://localhost:5000/API/product/1")
    return product.json()


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
def products_json():
    products = requests.get("http://localhost:5000/API/products")
    return products.json()


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
