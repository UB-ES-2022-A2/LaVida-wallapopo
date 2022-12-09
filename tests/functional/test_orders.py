import base64



def test_post_orders(client):
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
        json = {'product_id': 99, 'credit_card': 1234567890, 'cvc': 123,
                'cc_exp_date': '05/25', 'cc_owner': 'Pepe'}

        # Test sending request with non-existent user
        r = client.post("API/order/add/pepe433@gmail.com", json=json, headers=headers)
        assert r.status_code == 409
        assert r.json == {'message': 'account with email [pepe433@gmail.com] does not exist'}

        # Test invalid access with non-matching usernames between current user and request user
        r = client.post("API/order/add/killer23@gmail.com", json=json, headers=headers)
        assert r.status_code == 400
        assert r.json == {'message': "Bad authorization user"}

        # Test sending request with non-existent product
        r = client.post("API/order/add/pepe432@gmail.com", json=json, headers=headers)
        assert r.status_code == 409
        assert r.json == {'message': "product with id [99] doesn't exist"}

        json['product_id'] = 1
        # Test a valid order with valid user
        r = client.post("API/order/add/pepe432@gmail.com", json=json, headers=headers)
        assert r.status_code == 200
        assert r.json['product']['status'] == 'Vendido'


def test_get_sales(client):
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
        # Test retrieving sales with non-existing user
        r = client.get("API/order/sales/pepe433@gmail.com", headers=headers)
        assert r.status_code == 404
        assert r.json == {'message': 'This email [pepe433@gmail.com] does not exist'}

        # Test invalid access with non-matching usernames between current user and request user
        r = client.get("API/order/sales/killer23@gmail.com", headers=headers)
        assert r.status_code == 400
        assert r.json == {'message': "Bad authorization user"}

        # Test retrieving all user's sales (non-sold products)
        r = client.get("API/order/sales/pepe432@gmail.com", headers=headers)
        assert r.status_code == 200
        assert r.json['orders_list'] == []

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
        killer_token = killer_login.json
        killer_headers = {'Authorization': 'Basic {}'.format(base64.b64encode('{token}:{password}'.format(
            token=killer_token['token'], password='').encode()).decode())
        }
        assert killer_login.status_code == 200

        # Buy product from other user
        json = {'product_id': 5, 'credit_card': 1234567890, 'cvc': 123,
                'cc_exp_date': '05/25', 'cc_owner': 'Pedro'}
        r = client.post("API/order/add/killer23@gmail.com", json=json, headers=killer_headers)
        assert r.status_code == 200
        assert r.json['product']['status'] == 'Vendido'

        # Logout to end current session
        r = client.post("API/logout/killer23@gmail.com", json=killer_json, headers=killer_headers)
        assert r.status_code == 200

        # Login as the first user
        json = {'email': 'pepe432@gmail.com', 'username': 'pepeman', 'password': 'pepe123,.'}
        login = client.post("API/login", json=json)
        token = login.json
        headers = {'Authorization': 'Basic {}'.format(base64.b64encode('{token}:{password}'.format(
            token=token['token'], password='').encode()).decode())
                   }
        assert login.status_code == 200

        # Test retrieving all user's sold products
        r = client.get("API/order/sales/pepe432@gmail.com", headers=headers)
        assert r.status_code == 200
        assert r.json['orders_list'][-1]['product']['name'] == "Nintendo Switch"


def test_get_purchases(client):
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
        # Test retrieving purchases with non-existing user
        r = client.get("API/order/sales/pepe433@gmail.com", headers=headers)
        assert r.status_code == 404
        assert r.json == {'message': 'This email [pepe433@gmail.com] does not exist'}

        # Test invalid access with non-matching usernames between current user and request user
        r = client.get("API/order/sales/killer23@gmail.com", headers=headers)
        assert r.status_code == 400
        assert r.json == {'message': "Bad authorization user"}

        # Test retrieving all user's purchased products (currently non-purchased products)
        r = client.get("API/order/purchases/pepe432@gmail.com", headers=headers)
        assert r.status_code == 200
        assert r.json['orders_list'] == []

        # Buy a product from another user
        json = {'product_id': 1, 'credit_card': 1234567890, 'cvc': 123,
                'cc_exp_date': '05/25', 'cc_owner': 'Pepe'}
        r = client.post("API/order/add/pepe432@gmail.com", json=json, headers=headers)
        assert r.status_code == 200
        assert r.json['product']['status'] == 'Vendido'

        # Test retrieving all user's purchased products
        r = client.get("API/order/purchases/pepe432@gmail.com", headers=headers)
        assert r.status_code == 200
        assert r.json['orders_list'][-1]['product']['name'] == "Oso de peluche"
