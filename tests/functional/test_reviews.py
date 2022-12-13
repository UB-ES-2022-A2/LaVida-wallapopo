import base64


def test_post_reviews(client):
    with client:
        # Login
        json = {'email': 'pepe432@gmail.com', 'username': 'pepeman', 'password': 'pepe123,.'}
        login = client.post("API/login", json=json)
        assert login.status_code == 200

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
        json = {'email': 'pepe433@gmail.com', 'product_id': 99, 'stars': 4, 'comment': 'Estaba un poco sucio'}

        # Test sending request with non-existent user
        r = client.post("API/reviews", json=json, headers=headers)
        assert r.status_code == 409
        assert r.json == {'message': 'account with email [pepe433@gmail.com] does not exist'}

        # Test invalid access with non-matching usernames between current user and request user
        json['email'] = 'killer23@gmail.com'
        r = client.post("API/reviews", json=json, headers=headers)
        assert r.status_code == 400
        assert r.json == {'message': "Bad authorization user"}

        json['email'] = 'pepe432@gmail.com'
        # Test sending request with non-existent product
        r = client.post("API/reviews", json=json, headers=headers)
        assert r.status_code == 409
        assert r.json == {'message': "product with id [99] doesn't exist"}

        json['product_id'] = 1
        # Test reviewing a seller from a non-purchased product
        r = client.post("API/reviews", json=json, headers=headers)
        assert r.status_code == 409
        assert r.json == {'message': "user with email [pepe432@gmail.com] hasn't purchased product with id [1]"}

        # Buy a product from another user
        purchase_json = {'product_id': 1, 'credit_card': 1234567890, 'cvc': 123,
                         'cc_exp_date': '05/25', 'cc_owner': 'Pepe'}
        purchase_request = client.post("API/order/add/pepe432@gmail.com", json=purchase_json, headers=headers)
        assert purchase_request.status_code == 200
        assert purchase_request.json['product']['status'] == 'Vendido'

        # Test reviewing the seller of the purchased product
        r = client.post("API/reviews", json=json, headers=headers)
        assert r.status_code == 200
        assert r.json['reviewed']['email'] == purchase_request.json['seller']['email']
        assert r.json['reviewer']['email'] == purchase_request.json['buyer']['email']
        assert r.json['product']['id'] == purchase_request.json['product']['id']


def test_get_reviews(client):
    with client:
        # Login
        json = {'email': 'pepe432@gmail.com', 'username': 'pepeman', 'password': 'pepe123,.'}
        login = client.post("API/login", json=json)
        assert login.status_code == 200

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

        # Test sending request with non-existent user
        r = client.get("API/reviews/pepe433@gmail.com", headers=headers)
        assert r.status_code == 404
        assert r.json == {'message': 'account with email [pepe433@gmail.com] does not exist'}

        # Test invalid access with non-matching usernames between current user and request user
        r = client.get("API/reviews/killer23@gmail.com", headers=headers)
        assert r.status_code == 400
        assert r.json == {'message': "Bad authorization user"}

        # Test retrieving all reviews (no reviews received)
        r = client.get("API/reviews/pepe432@gmail.com", headers=headers)
        assert r.status_code == 200
        assert r.json == {"reviews_list": []}

        product_json = {
            'name': 'Nintendo Switch', 'category': 'Consolas y Videojuegos', 'price': 150,
            'condition': 'Casi nuevo', 'description': 'La vendo porque apenas la uso y necesito algo de dinero',
            'shipment': False
        }
        # Add product with current user
        r = client.post("API/catalog/add/pepe432@gmail.com", json=product_json, headers=headers)
        assert r.status_code == 200

        # Logout to end current session
        r = client.post("API/logout/pepe432@gmail.com", json=json, headers=headers)
        assert r.status_code == 200

        # Login as another user
        killer_json = {'email': 'killer23@gmail.com', 'username': 'the killer god', 'password': 'magic_p443.'}
        killer_login = client.post("API/login", json=killer_json)
        assert login.status_code == 200

        killer_token = killer_login.json
        killer_headers = {'Authorization': 'Basic {}'.format(base64.b64encode('{token}:{password}'.format(
            token=killer_token['token'],
            password='').encode()).decode())
        }

        # Buy a product from the previous user
        purchase_json = {'product_id': 5, 'credit_card': 1234567890, 'cvc': 123,
                         'cc_exp_date': '05/25', 'cc_owner': 'Pepe'}
        purchase_request = client.post("API/order/add/killer23@gmail.com", json=purchase_json, headers=killer_headers)
        assert purchase_request.status_code == 200
        assert purchase_request.json['product']['status'] == 'Vendido'

        # Add a review to the seller
        json = {'email': 'killer23@gmail.com', 'product_id': 5, 'stars': 5, 'comment': 'Entrega en muy buen estado'}
        r = client.post("API/reviews", json=json, headers=killer_headers)
        assert r.status_code == 200

        # Logout to end current session
        r = client.post("API/logout/killer23@gmail.com", json=killer_json, headers=killer_headers)
        assert r.status_code == 200

        # Login as the first user
        json = {'email': 'pepe432@gmail.com', 'username': 'pepeman', 'password': 'pepe123,.'}
        login = client.post("API/login", json=json)
        assert login.status_code == 200
        token = login.json
        headers = {'Authorization': 'Basic {}'.format(base64.b64encode('{token}:{password}'.format(
            token=token['token'],
            password='').encode()).decode())
        }

        # Test retrieving all received reviews
        r = client.get("API/reviews/pepe432@gmail.com", headers=headers)
        assert r.status_code == 200
        assert r.json['reviews_list'][0]['product_id'] == 5
        assert r.json['reviews_list'][0]['reviewed']['email'] == 'pepe432@gmail.com'
        assert r.json['reviews_list'][0]['reviewer']['email'] == 'killer23@gmail.com'
