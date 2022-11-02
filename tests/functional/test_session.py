from app import app
import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:5000/"


def test_login_post():
    # Test an invalid login with wrong format email
    json = {'email': 'pepe432gmail.com', 'password': 'pepe123,.'}
    wrong_email_format = requests.post(url + "API/login", json)
    assert wrong_email_format.status_code == 400
    assert wrong_email_format.json() == {'message': 'Email [pepe432gmail.com] is not a valid format'}

    # Test an invalid login with nonexistent email address
    json = {'email': 'pepe433@gmail.com', 'password': 'pepe123,.'}
    account_not_exist = requests.post(url + "API/login", json)
    assert account_not_exist.status_code == 404
    assert account_not_exist.json() == {'message': "Account with email [pepe433@gmail.com] does not exist"}

    # Test an invalid login with missing password
    json = {'email': 'pepe433@gmail.com', 'password': None}
    blank_password = requests.post(url + "API/login", json)
    assert blank_password.status_code == 400
    assert blank_password.json() == {'message': {'password': 'This field cannot be left blank'}}

    # Test an invalid login with non-matching credentials
    json = {'email': 'pepe432@gmail.com', 'password': 'pepe1234.'}
    wrong_password = requests.post(url + "API/login", json)
    assert wrong_password.status_code == 400
    assert wrong_password.json() == {'message': "Email or Password are incorrect"}

    # Test a valid login
    json = {'email': 'pepe432@gmail.com', 'password': 'pepe123,.'}
    login = requests.post(url + "API/login", json)
    assert login.status_code == 200


def test_logout_post():
    # Test a valid login
    json = {'email': 'pepe432@gmail.com', 'username': 'pepeman', 'password': 'pepe123,.'}
    login = requests.post(url + "API/login", json)
    assert login.status_code == 200

    # Test an invalid logout with nonexistent email
    token = login.json()
    auth = HTTPBasicAuth(token['token'], '')
    r = requests.post(url + "API/logout/pepe433@gmail.com", auth=auth)
    assert r.status_code == 404
    assert r.json() == {'message': 'This email [pepe433@gmail.com] does not exist'}

    # Test an invalid logout with non-matching usernames between current user and request user
    json = {'email': 'killer23@gmail.com', 'password': 'magic_p443.'}
    requests.post(url + "API/login", json)
    r = requests.post(url + "API/logout/killer23@gmail.com", auth=auth)
    assert r.status_code == 400
    assert r.json() == {'message': "Bad authorization user"}

    # Test a valid logout
    r = requests.post(url + "API/logout/pepe432@gmail.com", auth=auth)
    assert r.status_code == 200
    assert r.json() == {'message': 'Logged out'}
