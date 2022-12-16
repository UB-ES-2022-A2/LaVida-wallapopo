def test_accounts_get(client):
    with client:
        # Test a valid login
        json = {'email': 'pepe432@gmail.com', 'password': 'pepe123,.'}
        login = client.post("API/login", json=json)
        assert login.status_code == 200

        # Test invalid access with nonexistent email
        token = login.json
        import base64
        headers = {
            'Authorization': 'Basic {}'.format(
                base64.b64encode(
                    '{token}:{password}'.format(
                        token=token['token'],
                        password='').encode()
                ).decode()
            )
        }

        r = client.get("API/account/pepe433@gmail.com", headers=headers)
        assert r.status_code == 404
        assert r.json == {'message': 'This email [pepe433@gmail.com] does not exist'}

        # Test invalid access with non-matching usernames between current user and request user
        json = {'email': 'killer23@gmail.com', 'password': 'magic_p443.'}
        client.post("API/login", json=json)
        r = client.get("API/account/killer23@gmail.com", headers=headers)
        assert r.status_code == 400
        assert r.json == {'message': "Bad authorization user"}

        r = client.get("API/account/pepe432@gmail.com", headers=headers)
        expected = {
            'account': {
                'birthday': None,
                'confirmed': True,
                'email': 'pepe432@gmail.com',
                'is_admin': 0,
                'name': None,
                'surname': None,
                'username': 'pepeman',
                'profile': 'https://storage.googleapis.com/wallapopo-img/default-profile.jpg'
            }
        }

        assert r.status_code == 200
        assert r.json == expected


def test_accounts_post(client):
    with client:
        # Test invalid register with missing data
        json = {'username': 'dummyname', 'email': 'dummygmail.com', 'password': 'dummy12.'}
        r = client.post("API/account", json=json)
        assert r.status_code == 400
        assert r.json == {'message': 'Email [dummygmail.com] is not a valid format'}

        # Test invalid register with already existing email
        json = {'username': 'pepeman', 'email': 'pepe432@gmail.com', 'password': 'pepe123,.'}
        r = client.post("API/account", json=json)
        assert r.status_code == 409
        assert r.json == {'message': 'Account with email [pepe432@gmail.com] already exist'}

        # Test invalid register with already existing email
        json = {'username': 'pepeman', 'email': 'dummy@gmail.com', 'password': 'dummy123,.'}
        r = client.post("API/account", json=json)
        assert r.status_code == 409
        assert r.json == {'message': 'Username [pepeman] is already in use'}

        json = {'username': 'dummyUser', 'email': 'dummy@gmail.com', 'password': 'hola'}
        r = client.post("API/account", json=json)
        assert r.status_code == 409
        assert r.json == {'message': 'Password is necessary to register'}

        json = {'username': None, 'email': 'dummy@gmail.com', 'password': 'dummy12.'}
        r = client.post("API/account", json=json)
        assert r.status_code == 500
        assert r.json == {'message': 'Error while creating new account'}

        # Test valid register
        json = {'username': 'dummyname', 'email': 'dummy@gmail.com', 'password': 'dummy12.'}
        r = client.post("API/account", json=json)
        expected = {
                        'birthday': None,
                        'confirmed': False,
                        'email': 'dummy@gmail.com',
                        'is_admin': 0,
                        'name': None,
                        'surname': None,
                        'username': 'dummyname',
                        'profile': 'https://storage.googleapis.com/wallapopo-img/default-profile.jpg'
                        }

        assert r.status_code == 200
        assert r.json == expected
