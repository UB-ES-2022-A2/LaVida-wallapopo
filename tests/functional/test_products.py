import requests
url = "http://localhost:5000/"


def test_products_get(first_product):
    r = requests.get(url + "API/product/1")
    print(r.json())

    assert r.status_code == 200
    assert r.json() == first_product

    r = requests.get(url + "API/product/0")
    assert r.status_code == 500  # 404


def test_products_list_get(products_json):
    r = requests.get(url + "API/products")
    assert r.json() == products_json


def test_add_product_post(user_auth):
    json = {
        'name': 'Nintendo Switch',
        'category': 'Consolas y Videojuegos',
        'price': 150,
        'condition': 'Casi nuevo',
        'description': 'La vendo porque apenas la uso y necesito algo de dinero',
        'shipment': False
    }

    # Test empty fields
    r = requests.post(url + "API/catalog/add/pepe432@gmail.com", auth=user_auth)
    assert r.status_code == 400
    assert r.json() == {'message': {'name': 'This field cannot be left blank'}}

    r = requests.post(url + "API/catalog/add/pepe433@gmail.com", json, auth=user_auth)
    assert r.status_code == 404
    assert r.json() == {'message': 'This email [pepe433@gmail.com] does not exist'}

    # TODO: Search how to test that the username of the current user and the username of the request are different
    """
    r = requests.post(url + "API/catalog/add/killer23@gmail.com", auth=auth)
    assert r.status_code == 400
    assert r.json() == {'message': "Bad authorization user"}
    """

    # TODO: Add test for the addition of a new product that can be repeated (do not save in the DB permanently)

    r = requests.post(url + "API/catalog/add/pepe432@gmail.com", json, auth=user_auth)

    date = r.json()['date']
    product_data = {
        'category': 'Consolas y Videojuegos',
        'condition': 'Casi nuevo',
        'date': date,
        'description': 'La vendo porque apenas la uso y necesito algo de dinero',
        'id': 5,
        'image': 'product_placeholder.png',
        'name': 'Nintendo Switch',
        'price': 150.0,
        'status': 'En venta',
        'user': 'pepe432@gmail.com'
    }
    assert r.status_code == 200
    assert r.json() == product_data

