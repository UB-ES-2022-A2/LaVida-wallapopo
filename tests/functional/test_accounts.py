import requests
from requests.auth import HTTPBasicAuth

url = "http://127.0.0.1:5000/"


def test_accounts_get(client):
    with client:
        # Test a valid login
        json = {'email': 'pepe432@gmail.com', 'password': 'pepe123,.'}
        login = requests.post(url + "API/login", json=json)
        assert login.status_code == 200

        # Test invalid access with nonexistent email
        token = login.json()
        auth = HTTPBasicAuth(token['token'], '')

        r = requests.get(url + "API/account/pepe433@gmail.com", auth=auth)
        assert r.status_code == 404
        assert r.json() == {'message': 'This email [pepe433@gmail.com] does not exist'}

        # Test invalid access with non-matching usernames between current user and request user
        json = {'email': 'killer23@gmail.com', 'password': 'magic_p443.'}
        requests.post(url + "API/login", json=json)
        r = requests.get(url + "API/account/killer23@gmail.com", auth=auth)
        assert r.status_code == 400
        assert r.json() == {'message': "Bad authorization user"}

        r = requests.get(url + "API/account/pepe432@gmail.com", auth=auth)
        expected = {
            'account': {
                'birthday': None,
                'confirmed': True,
                'email': 'pepe432@gmail.com',
                'is_admin': 0,
                'name': None,
                'surname': None,
                'username': 'pepeman'
            }
        }

        assert r.status_code == 200
        assert r.json() == expected


def test_accounts_post(_app, client):
    with _app.app_context():
        # Test invalid register with missing data
        json = {'username': 'dummyname', 'email': None, 'password': 'dummy12.'}
        r = requests.post(url + "API/account", json=json)
        assert r.status_code == 500

        json = {'username': 'dummyname', 'email': 'dummy@gmail.com', 'password': None}
        r = requests.post(url + "API/account", json=json)
        assert r.status_code == 500

        json = {'username': None, 'email': 'dummy@gmail.com', 'password': 'dummy12.'}
        r = requests.post(url + "API/account", json=json)
        assert r.status_code == 500
        assert r.json() == {'message': 'Error while creating new account'}

        # Test invalid register with already existing email
        json = {'username': 'pepeman', 'email': 'pepe432@gmail.com', 'password': 'pepe123,.'}
        r = requests.post(url + "API/account", json=json)
        assert r.status_code == 409
        assert r.json() == {'message': 'Account with email [pepe432@gmail.com] already exist'}

        # Test valid register
        json = {'username': 'dummyname', 'email': 'dummy@gmail.com', 'password': 'dummy12.'}
        with client:
            r = requests.post(url + "API/account", json=json)
            expected = {
                        'birthday': None,
                        'confirmed': False,
                        'email': 'dummy@gmail.com',
                        'is_admin': 0,
                        'name': None,
                        'surname': None,
                        'username': 'dummyname'
                        }

            assert r.status_code == 200
            assert r.json() == expected


