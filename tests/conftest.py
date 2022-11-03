import pytest

import requests
from requests.auth import HTTPBasicAuth
from models.accounts import AccountsModel
from models.products import ProductsModel


# --------
# Fixtures
# --------
@pytest.fixture(scope='function')
def first_product():
    product = requests.get("http://localhost:5000/API/product/1")
    return product.json()


@pytest.fixture(scope='function')
def dummy_user():
    acc = AccountsModel("dummy@gmail.com", "dummyname")
    acc.password = "qwerty12."
    return acc


@pytest.fixture(scope='function')
def dummy_password(dummy_user):
    dummy_user.hash_password(dummy_user.password)
    return dummy_user.password


@pytest.fixture(scope='function')
def switch_product():
    p = ProductsModel("Nintendo Switch", "Consolas y Videojuegos", "Apenas la uso y necesito dinero", 150, "Casi nuevo")
    return p


@pytest.fixture(scope='function')
def pepe_products():
    p = ProductsModel.get_all_by_user("pepe432@gmail.com")
    return p


@pytest.fixture(scope='function')
def user_auth():
    json = {'email': 'pepe432@gmail.com', 'password': 'pepe123,.'}
    login = requests.post("http://localhost:5000/API/login", json)
    token = login.json()
    auth = HTTPBasicAuth(token['token'], '')
    return auth


@pytest.fixture(scope='function')
def products_json():
    products = requests.get("http://localhost:5000/API/products")
    return products.json()
