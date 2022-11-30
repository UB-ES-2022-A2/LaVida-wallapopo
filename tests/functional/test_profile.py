import base64


def test_get_profile(client, auth_header):
    with client:
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
        r = client.get("API/profile/pepe433@gmail.com", headers=headers)
        assert r.status_code == 404
        assert r.json == {'message': 'This email [pepe433@gmail.com] does not exist'}

        # Test invalid access with non-matching usernames between current user and request user
        r = client.get("API/profile/killer23@gmail.com", headers=headers)
        assert r.status_code == 401
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
                'username': 'pepeman'
            }
        }

        assert r.status_code == 200
        assert r.json == expected


def test_put_profile(client):
    with client:
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
        # Test nonexistent email
        json = {'email': 'pepe433@gmail.com', 'image': 'imagen.png', 'name': 'Pepe', 'surname': 'Márquez',
                'birthday': '2000-11-30'}
        r = client.put("API/profile/pepe433@gmail.com", json=json, headers=headers)
        assert r.status_code == 404
        assert r.json == {'message': 'This email [pepe433@gmail.com] does not exist'}

        # Test non-matching email between current user and request user's email
        json = {'email': 'killer23@gmail.com', 'image': 'imagen.png', 'name': 'Dolores', 'surname': 'Fuertes',
                'birthday': '2000-11-30'}
        r = client.put("API/profile/killer23@gmail.com", json=json, headers=headers)
        assert r.status_code == 401
        assert r.json == {'message': 'Bad authorization user'}

        # Test valid profile update
        json = {'email': 'pepe432@gmail.com', 'image': 'imagen.png', 'name': 'Pepe', 'surname': 'Márquez',
                'birthday': '2020-11-30'}
        r = client.put("API/profile/pepe432@gmail.com", json=json, headers=headers)
        assert r.status_code == 200
        assert r.json == {'message': "Profile updated successfully"}
