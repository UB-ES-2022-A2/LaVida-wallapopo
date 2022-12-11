from models.favourites import FavouritesModel
import datetime


def test_create_favourite():
    fav = FavouritesModel('admin123@gmail.com', 1)
    assert fav.user_id == 'admin123@gmail.com'
    assert fav.product_id == 1


def test_json(_app, dummy_favourite):
    with _app.app_context():
        expected = {'id': 1,
                    'user': {'email': 'admin123@gmail.com',
                             'username': 'The God',
                             'name': None,
                             'surname': None,
                             'birthday': None,
                             'is_admin': 0,
                             'confirmed': True},
                    'product': dummy_favourite[1].json()
                    }
        assert dummy_favourite[0].json() == expected


def test_get_all(_app, dummy_favourite):
    with _app.app_context():
        result = len(FavouritesModel.get_all())
        assert result == 1


def test_get_fav_by_email(_app, dummy_favourite):
    with _app.app_context():
        result = FavouritesModel.get_by_email("pepe432@gmail.com")
        assert len(result) == 0
        result = FavouritesModel.get_by_email("admin123@gmail.com")
        assert len(result) == 1


def test_save_favourite(_app):
    with _app.app_context():
        previous = len(FavouritesModel.get_all())
        r = FavouritesModel('admin123@gmail.com', 1)
        FavouritesModel.save_to_db(r)
        result = len(FavouritesModel.get_all())

        assert previous == 0
        assert result == 1


def test_delete_favourite(_app, dummy_favourite):
    with _app.app_context():
        previous = len(FavouritesModel.get_all())
        FavouritesModel.delete_from_db(dummy_favourite[0])
        result = len(FavouritesModel.get_all())

        assert previous == 1
        assert result == 0
