from app import app
import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:5000/"


def test_accounts_get():
    with app.test_client():
        # Test a valid login
        json = {'email': 'pepe432@gmail.com', 'password': 'pepe123,.'}
        login = requests.post(url + "API/login", json)
        assert login.status_code == 200

        # Test invalid access with nonexistent email
        token = login.json()
        auth = HTTPBasicAuth(token['token'], '')

        r = requests.get(url + "API/account/pepe433@gmail.com", auth=auth)
        assert r.status_code == 404
        assert r.json() == {'message': 'This email [pepe433@gmail.com] does not exist'}

        # Test invalid access with non-matching usernames between current user and request user
        json = {'email': 'killer23@gmail.com', 'password': 'magic_p443.'}
        requests.post(url + "API/login", json)
        r = requests.get(url + "API/account/killer23@gmail.com", auth=auth)
        assert r.status_code == 400
        assert r.json() == {'message': "Bad authorization user"}

        r = requests.get(url + "API/account/pepe432@gmail.com", auth=auth)
        expected = {
            'account': {
                'birthday': None,
                'email': 'pepe432@gmail.com',
                'is_admin': 0,
                'name': None,
                'surname': None,
                'username': 'pepeman'
            }
        }

        assert r.status_code == 200
        assert r.json() == expected


def test_accounts_post():
    # Test invalid register with missing email
    json = "{'username': 'dummyname', 'email': None, 'password': 'dummy12.'}"
    account = requests.post(url + "API/account", json)
    assert account.status_code == 400
    assert account.json() == {'message': {'email': 'This field cannot be left blank'}}

    # Test invalid register with missing username
    json = {'username': None, 'email': 'dummy@gmail.com', 'password': 'dummy12.'}
    account = requests.post(url + "API/account", json)
    assert account.status_code == 400
    assert account.json() == {'message': {'username': 'This field cannot be left blank'}}

    # Test invalid register with missing password
    json = {'username': 'dummyname', 'email': 'dummy@gmail.com', 'password': None}
    account = requests.post(url + "API/account", json)
    assert account.status_code == 400
    assert account.json() == {'message': {'password': 'This field cannot be left blank'}}

    # Test invalid register with already existing email
    json = {'username': 'pepeman', 'email': 'pepe432@gmail.com', 'password': 'pepe123,.'}
    account = requests.post(url + "API/account", json)
    assert account.status_code == 409
    assert account.json() == {'message': 'Account with email [pepe432@gmail.com] already exist'}

    # Test valid register
    # TODO: Add test for the registration of a new account that can be repeated (do not save in the DB permanently)
    json = {'username': 'dummyname', 'email': 'dummy@gmail.com', 'password': 'dummy12.'}
    with app.test_client():
        account = requests.post(url + "API/account", json)
        expected = {
                    'birthday': None,
                    'email': 'dummy@gmail.com',
                    'is_admin': 0,
                    'name': None,
                    'surname': None,
                    'username': 'dummyname'
                    }

        assert account.status_code == 200
        assert account.json() == expected


