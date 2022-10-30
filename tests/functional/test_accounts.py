import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:5000/"


def test_accounts_get():
    json = {'email': 'pepe432@gmail.com', 'password': 'pepe123,.'}
    login = requests.post(url + "login", json)
    assert login.status_code == 200

    token = login.json()
    auth = HTTPBasicAuth(token['token'], '')

    r = requests.get(url + "account/pepe433@gmail.com", auth=auth)
    assert r.status_code == 404
    assert r.json() == {'message': 'This email [pepe433@gmail.com] does not exist'}

    # TODO: Search how to test that the username of the current user and the username of the request are different
    """
    r = requests.get(url + "account/killer23@gmail.com", auth=auth)
    assert r.status_code == 400
    assert r.json() == {'message': "Bad authorization user"}
    """

    r = requests.get(url + "account/pepe432@gmail.com", auth=auth)
    assert r.status_code == 200


def test_accounts_post():
    json = "{'username': 'dummyname', 'email': None, 'password': 'dummy12.'}"
    account = requests.post(url + "account", json)
    assert account.status_code == 400
    assert account.json() == {'message': {'email': 'This field cannot be left blank'}}

    json = {'username': None, 'email': 'dummy@gmail.com', 'password': 'dummy12.'}
    account = requests.post(url + "account", json)
    assert account.status_code == 400
    assert account.json() == {'message': {'username': 'This field cannot be left blank'}}

    json = {'username': 'dummyname', 'email': 'dummy@gmail.com', 'password': None}
    account = requests.post(url + "account", json)
    assert account.status_code == 400
    assert account.json() == {'message': {'password': 'This field cannot be left blank'}}

    json = {'username': 'pepeman', 'email': 'pepe432@gmail.com', 'password': 'pepe123,.'}
    account = requests.post(url + "account", json)
    assert account.status_code == 409
    assert account.json() == {'message': 'Account with email [pepe432@gmail.com] already exist'}

    # TODO: Add test for the registration of a new account that can be repeated (do not save in the DB permanently)
    """
    json = "{'username': 'dummyname', 'email': 'dummy@gmail.com', 'password': 'dummy12.'}"
    account = requests.post(url + "account", json)
    assert account.status_code == 200
    """


