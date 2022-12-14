from models.accounts import AccountsModel


def test_create_user():
    acc = AccountsModel("dummy@gmail.com", "dummyname", False)
    acc.password = "qwerty12."

    assert acc.email == "dummy@gmail.com"
    assert acc.username == "dummyname"
    assert acc.is_admin == 0
    assert acc.confirmed is False
    assert acc.password == "qwerty12."


def test_json(dummy_user):
    expected = {
        'email': 'dummy@gmail.com',
        'username': 'dummyname',
        'name': None, 'surname': None,
        'birthday': None, 'is_admin': 0,
        'confirmed': False,
        'profile': None
    }
    assert dummy_user.json() == expected


def test_get_all(_app):
    with _app.app_context():
        result = AccountsModel.get_all()
        expected = "[<AccountsModel admin123@gmail.com>, <AccountsModel pepe432@gmail.com>, <AccountsModel juan35@hotmail.com>, <AccountsModel killer23@gmail.com>, <AccountsModel joseramon33@hotmail.com>]"
        assert str(result) == expected


def test_get_by_email(_app):
    with _app.app_context():
        result = AccountsModel.get_by_email("pepe432@gmail.com")
        expected = "<AccountsModel pepe432@gmail.com>"
        assert str(result) == expected


def test_get_by_username(_app):
    with _app.app_context():
        result = AccountsModel.get_by_username("pepeman")
        expected = "<AccountsModel pepe432@gmail.com>"
        assert str(result) == expected


def test_get_user_roles(dummy_user):
    role = dummy_user.get_user_roles()

    assert str(role) == "['user']"
    assert str(role) != "['admin']"


def test_save_user(_app, dummy_user):
    with _app.app_context():
        previous = len(AccountsModel.get_all())
        AccountsModel.save_to_db(dummy_user)
        result = len(AccountsModel.get_all())

        assert previous == 5
        assert result == 6


def test_delete_user(_app):
    with _app.app_context():
        previous = len(AccountsModel.get_all())
        user = AccountsModel.get_by_email("pepe432@gmail.com")
        AccountsModel.delete_from_db(user)
        result = len(AccountsModel.get_all())

        assert previous == 5
        assert result == 4


def test_store_token(_app, dummy_user):
    with _app.app_context():
        AccountsModel.save_to_db(dummy_user)
        t = dummy_user.generate_auth_token()
        dummy_user.store_token(t)

        assert t == dummy_user.current_token
        AccountsModel.delete_from_db(dummy_user)


def test_verify_token(_app, dummy_user):
    with _app.app_context():
        AccountsModel.save_to_db(dummy_user)
        t = dummy_user.generate_auth_token()
        dummy_user.store_token(t)
        u = AccountsModel.verify_auth_token(t)

        assert str(u) == "<AccountsModel dummy@gmail.com>"
        AccountsModel.delete_from_db(dummy_user)


def test_invalidate_token(_app, dummy_user):
    with _app.app_context():
        AccountsModel.save_to_db(dummy_user)
        t = dummy_user.generate_auth_token()
        dummy_user.invalidate_auth_token()
        u = AccountsModel.verify_auth_token(t)

        assert u != "<AccountsModel dummy@gmail.com>"
        assert u is None
        AccountsModel.delete_from_db(dummy_user)

