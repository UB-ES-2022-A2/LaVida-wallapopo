import pytest

import requests
from requests.auth import HTTPBasicAuth


# --------
# Fixtures
# --------
@pytest.fixture(scope='module')
def first_product():
    p = {
        'category': 'Niños y Bebés',
        'condition': 'Nuevo',
        'date': '2022-11-01T09:45:50',
        'description': 'oso de peluche viejo pero en buen estado',
        'id': 1,
        'image': 'Oso.jpeg',
        'name': 'Oso de peluche',
        'price': 4.0,
        'status': 'En venta',
        'user': 'pepe432@gmail.com'
    }
    return p


@pytest.fixture(scope='module')
def user_auth():
    json = {'email': 'pepe432@gmail.com', 'password': 'pepe123,.'}
    login = requests.post("http://localhost:5000/API/login", json)
    token = login.json()
    auth = HTTPBasicAuth(token['token'], '')
    return auth

@pytest.fixture(scope='module')
def products_json():
    products = requests.get("http://localhost:5000/API/products")
    return products.json()
