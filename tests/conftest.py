import pytest

import requests


# --------
# Fixtures
# --------

@pytest.fixture(scope='module')
def products_json():
    products = requests.get("http://localhost:5000/products")
    return products.json()
