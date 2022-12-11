import base64


def test_post_favourites(client):
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
        json = {'email': 'pepe433@gmail.com', 'product_id': 99}

        # Test sending request with non-existent user
        r = client.post("API/favourites", json=json, headers=headers)
        assert r.status_code == 409
        assert r.json == {'message': 'account with email [pepe433@gmail.com] does not exist'}

        # Test invalid access with non-matching usernames between current user and request user
        json['email'] = 'killer23@gmail.com'
        r = client.post("API/favourites", json=json, headers=headers)
        assert r.status_code == 400
        assert r.json == {'message': "Bad authorization user"}

        json['email'] = 'pepe432@gmail.com'
        # Test sending request with non-existent product
        r = client.post("API/favourites", json=json, headers=headers)
        assert r.status_code == 409
        assert r.json == {'message': "product with id [99] doesn't exist"}

        json['product_id'] = 1
        # Test adding product to favourite
        r = client.post("API/favourites", json=json, headers=headers)
        assert r.status_code == 200

        # Test adding product that's already in favourite
        r = client.post("API/favourites", json=json, headers=headers)
        assert r.status_code == 409
        assert r.json == {'message': "product with id [1] is already in your favourite list"}


def test_get_favourites(client):
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
        r = client.get("API/favourites/pepe433@gmail.com", headers=headers)
        assert r.status_code == 404
        assert r.json == {'message': 'account with email [pepe433@gmail.com] does not exist'}

        # Test invalid access with non-matching usernames between current user and request user
        r = client.get("API/favourites/killer23@gmail.com", headers=headers)
        assert r.status_code == 400
        assert r.json == {'message': "Bad authorization user"}

        # Test retrieving all favourites (no favourites received)
        r = client.get("API/favourites/pepe432@gmail.com", headers=headers)
        assert r.status_code == 200
        assert r.json == {'favourites_list': []}

        json = {'email': 'pepe432@gmail.com', 'product_id': 1}

        # Test add one product to favourite
        r = client.post("API/favourites", json=json, headers=headers)
        assert r.status_code == 200

        # Test retrieving all favourites
        r = client.get("API/favourites/pepe432@gmail.com", headers=headers)
        assert r.status_code == 200
        assert r.json['favourites_list'] != []

def test_delete_favourites(client):
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
        json = {'email': 'pepe433@gmail.com', 'product_id': 99}

        # Test sending request with non-existent user
        r = client.delete("API/favourites", json=json, headers=headers)
        assert r.status_code == 409
        assert r.json == {'message': 'account with email [pepe433@gmail.com] does not exist'}

        # Test invalid access with non-matching usernames between current user and request user
        json['email'] = 'killer23@gmail.com'
        r = client.delete("API/favourites", json=json, headers=headers)
        assert r.status_code == 400
        assert r.json == {'message': "Bad authorization user"}

        json['email'] = 'pepe432@gmail.com'
        # Test sending request with non-existent product
        r = client.delete("API/favourites", json=json, headers=headers)
        assert r.status_code == 409
        assert r.json == {'message': "product with id [99] doesn't exist"}

        json['product_id'] = 1

        # Test deleting product that's not in favourite
        r = client.delete("API/favourites", json=json, headers=headers)
        assert r.status_code == 409
        assert r.json == {'message': "product with id [1] is not in your favourites list"}

        # Test adding product to favourite and delete it
        r = client.post("API/favourites", json=json, headers=headers)
        assert r.status_code == 200

        r = client.delete("API/favourites", json=json, headers=headers)
        assert r.status_code == 200
        assert r.json == {'message': "product with id [1] deleted from favourites"}

