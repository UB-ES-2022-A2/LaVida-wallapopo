import requests
from requests.auth import HTTPBasicAuth
import base64

url = "http://localhost:5000/"


def test_login_post(client):
    with client:
        # Test an invalid login with wrong format email
        json = {'email': 'pepe432gmail.com', 'password': 'pepe123,.'}
        wrong_email_format = client.post("API/login", json=json)
        assert wrong_email_format.status_code == 400
        assert wrong_email_format.json == {'message': 'Email [pepe432gmail.com] is not a valid format'}

        # Test an invalid login with nonexistent email address
        json = {'email': 'pepe433@gmail.com', 'password': 'pepe123,.'}
        account_not_exist = client.post("API/login", json=json)
        assert account_not_exist.status_code == 404
        assert account_not_exist.json == {'message': "Account with email [pepe433@gmail.com] does not exist"}

        # Test an invalid login with missing password
        json = {'email': 'pepe433@gmail.com', 'password': None}
        blank_password = client.post("API/login", json=json)
        assert blank_password.status_code == 404
        assert blank_password.json == {'message': "Account with email [pepe433@gmail.com] does not exist"}

        # Test an invalid login with non-matching credentials
        json = {'email': 'pepe432@gmail.com', 'password': 'pepe1234.'}
        wrong_password = client.post("API/login", json=json)
        assert wrong_password.status_code == 400
        assert wrong_password.json == {'message': "Email or Password are incorrect"}

        # Test a valid login
        json = {'email': 'pepe432@gmail.com', 'password': 'pepe123,.'}
        login = client.post("API/login", json=json)
        assert login.status_code == 200


def test_logout_post(client, auth_header):
    with client:
        # Test a valid login
        json = {'email': 'pepe432@gmail.com', 'username': 'pepeman', 'password': 'pepe123,.'}
        login = client.post("API/login", json=json)
        assert login.status_code == 200

        # Test an invalid logout with nonexistent email
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
        r = client.post("API/logout/pepe433@gmail.com", headers=headers)
        assert r.status_code == 404
        assert r.json == {'message': 'This email [pepe433@gmail.com] does not exist'}

        # Test an invalid logout with non-matching usernames between current user and request user
        json = {'email': 'killer23@gmail.com', 'password': 'magic_p443.'}
        client.post("API/login", json=json)
        r = client.post("API/logout/killer23@gmail.com", headers=headers)
        assert r.status_code == 400
        assert r.json == {'message': "Bad authorization user"}

        # Test a valid logout
        r = client.post("API/logout/pepe432@gmail.com", headers=headers)
        assert r.status_code == 200
        assert r.json == {'message': 'Logged out'}
