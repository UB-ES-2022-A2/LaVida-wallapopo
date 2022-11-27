import requests
from itsdangerous import URLSafeTimedSerializer

url = "http://localhost:5000/"


def test_validate_post(_app):
    with _app.app_context():
        # Try with invalid token
        json = {'validation_token': 'not_a_valid_token'}
        validation = requests.post(url + "API/validation", json=json)
        assert validation.status_code == 409
        assert validation.json() == {'message': "El link de verificación no es correcto"}

        # Using already verified account
        email = 'pepe432@gmail.com'
        serializer = URLSafeTimedSerializer(_app.config['SECRET_KEY'])
        token = serializer.dumps(email, salt=_app.config['SECURITY_PASSWORD_SALT'])
        json = {'validation_token': token}
        validation = requests.post(url + "API/validation", json=json)
        assert validation.status_code == 200
        assert validation.json() == {'message': "Tu cuenta ya estaba verificada. Puedes iniciar sesión."}

        # Verifying unverified account
        email = 'killer23@gmail.com'
        token = serializer.dumps(email, salt=_app.config['SECURITY_PASSWORD_SALT'])
        json = {'validation_token': token}
        validation = requests.post(url + "API/validation", json=json)
        assert validation.status_code == 200
        assert validation.json() == {'message': "Cuenta verificada correctamente! Puedes iniciar sesión."}
