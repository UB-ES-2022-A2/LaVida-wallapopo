import requests
url = "http://localhost:5000/"


def test_products_get(client, first_product):
    # Test a valid product retrieve
    from app import app
    #with client:
    #r = client.get(url + "API/product/1")
    r = requests.get(url + "API/product/1")
    assert r.status_code == 200
    assert r.json() == first_product

    # Test an invalid product retrieve
    r = requests.get(url + "API/product/0")
    assert r.status_code == 500  # 404


def test_products_list_get(_app, client, products_json):
    #with _app.test_request_context():
    # Test retrieving all products
    """
    r = client.get("API/products")
    assert r.status_code == 200
    assert r.json == products_json
    """
    r = requests.get(url + "API/products")
    assert r.status_code == 200
    assert r.json() == products_json




def test_add_product_post(_app, client, user_auth):
    with _app.app_context():
        json = {
            'name': None,
            'category': 'Consolas y Videojuegos',
            'price': 150,
            'condition': 'Casi nuevo',
            'description': 'La vendo porque apenas la uso y necesito algo de dinero',
            'shipment': False
        }
        """
        from requests import auth
        headers = {
            'Authorization': requests.auth._basic_auth_str('pepe432@gmail.com', 'pepe123,.')
        }
        autho=requests.auth._basic_auth_str('pepe432@gmail.com', 'pepe123,.')
        credentials = base64.b64encode(b"pepe432@gmail.com:pepe123,.")#.decode()
        passw = base64.b64encode(b"pepe123,.").decode()
        user = base64.b64encode(b"pepe432@gmail.com").decode()
        print("\nCRED: ", credentials)
        print("\nAUTH: ", "JWT",user_auth.__str__())
        print("\nAUTH: Authorization: Basic ", autho)
    
        # r = client.post("API/catalog/add/pepe432@gmail.com", json=json, headers={"Authorization": f"Basic {credentials.decode()}"})
        from werkzeug.datastructures import Authorization
        with client.session_transaction() as sess:
            sess['user_id'] = 'pepe432@gmail.com'
            sess['_fresh'] = True
        r=client.post("API/catalog/add/pepe432@gmail.com", json=json)# headers={"Authorization": user_auth})
        """
        r = requests.post(url + "API/catalog/add/pepe432@gmail.com", json=json, auth=user_auth)
        assert r.status_code == 500
        assert r.json() == {'message': 'Error while adding new product'}

        # Test empty fields
        r = requests.post(url + "API/catalog/add/pepe432@gmail.com", json=json, auth=user_auth)
        assert r.status_code == 500
        assert r.json() == {'message': 'Error while adding new product'}

        # Test nonexistent email
        r = requests.post(url + "API/catalog/add/pepe433@gmail.com", json=json, auth=user_auth)
        assert r.status_code == 404
        assert r.json() == {'message': 'This email [pepe433@gmail.com] does not exist'}

        # Test an invalid upload with non-matching usernames between current user and request user
        login_json = {'email': 'killer23@gmail.com', 'password': 'magic_p443.'}
        requests.post(url + "API/login", login_json)
        r = requests.post(url + "API/catalog/add/killer23@gmail.com", json=json, auth=user_auth)
        assert r.status_code == 400
        assert r.json() == {'message': "Bad authorization user"}

        # Test a valid product upload
        json['name'] = 'Nintendo Switch'
        r = requests.post(url + "API/catalog/add/pepe432@gmail.com", json=json, auth=user_auth)
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
            'shipment': False,
            'status': 'En venta',
            'user': 'pepe432@gmail.com',
            'username': 'pepeman'
        }
        assert r.status_code == 200
        assert r.json() == product_data

