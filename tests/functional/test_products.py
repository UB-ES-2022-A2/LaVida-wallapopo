import requests

url = "http://localhost:5000/"


def test_products_get(products_json):

    r = requests.get(url + "products")
    assert r.json() == products_json
