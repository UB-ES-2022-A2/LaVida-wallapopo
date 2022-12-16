def test_products_get(client, first_product):
    # Test a valid product retrieve
    with client:
        r = client.get("API/product/1")
        assert r.status_code == 200
        assert r.json == first_product

        # Test an invalid product retrieve
        r = client.get("API/product/0")
        assert r.status_code == 404


def test_products_list_get(client, products_json):
    # Test retrieving all products
    with client:
        r = client.get("API/products")
        assert r.status_code == 200
        assert r.json == products_json
        

def test_add_product_post(_app, client, auth_header):
    with client:
        json = {
            'name': None,
            'category': 'Consolas y Videojuegos',
            'price': 150,
            'condition': 'Casi nuevo',
            'description': 'La vendo porque apenas la uso y necesito algo de dinero',
            'shipment': False
        }

        r = client.post("API/catalog/add/pepe432@gmail.com", json=json, headers=auth_header)
        assert r.status_code == 500
        assert r.json == {'message': 'Error while adding new product'}

        # Test empty fields
        r = client.post("API/catalog/add/pepe432@gmail.com", json=json, headers=auth_header)
        assert r.status_code == 500
        assert r.json == {'message': 'Error while adding new product'}

        # Test nonexistent email
        r = client.post("API/catalog/add/pepe433@gmail.com", json=json, headers=auth_header)
        assert r.status_code == 404
        assert r.json == {'message': 'This email [pepe433@gmail.com] does not exist'}

        # Test an invalid upload with non-matching usernames between current user and request user
        login_json = {'email': 'killer23@gmail.com', 'password': 'magic_p443.'}
        client.post("API/login", json=login_json)
        r = client.post("API/catalog/add/killer23@gmail.com", json=json, headers=auth_header)
        assert r.status_code == 400
        assert r.json == {'message': "Bad authorization user"}

        # Test a valid product upload
        json['name'] = 'Nintendo Switch'
        r = client.post("API/catalog/add/pepe432@gmail.com", json=json, headers=auth_header)
        date = r.json['date']
        product_data = {
            'category': 'Consolas y Videojuegos',
            'condition': 'Casi nuevo',
            'date': date,
            'description': 'La vendo porque apenas la uso y necesito algo de dinero',
            'id': 5,
            'image': ['https://storage.googleapis.com/wallapopo-img/product_placeholder.png'],
            'name': 'Nintendo Switch',
            'price': 150.0,
            'shipment': False,
            'status': 'En venta',
            'user': 'pepe432@gmail.com',
            'username': 'pepeman',
            'user_image': 'https://storage.googleapis.com/wallapopo-img/default-profile.jpg'
        }
        assert r.status_code == 200
        assert r.json == product_data
