import datetime
from models.reviews import ReviewsModel


def test_create_review():
    r = ReviewsModel("pepe432@gmail.com", "killer23@gmail.com", 9, 4, "")

    assert r.reviewer_id == "pepe432@gmail.com"
    assert r.reviewed_id == "killer23@gmail.com"
    assert r.product_id == 9
    assert r.stars == 4
    assert r.comment == ""


def test_json(_app, dummy_review):
    with _app.app_context():
        current_date = datetime.date.today()
        user = dummy_review.json()['product']['user']
        username = dummy_review.json()['product']['username']
        assert dummy_review.json() == {'comment': '',
 'date': current_date.strftime('%Y-%m-%d'),
 'id': 1,
 'product': {'category': 'Otros',
             'condition': 'Casi nuevo',
             'date': current_date.strftime("%d-%b-%Y"),
             'description': 'juego de parchis edición retro',
             'id': 2,
             'image': 'Parchis.jpeg',
             'name': 'Parchis',
             'price': 20.0,
             'shipment': False,
             'status': 'En venta',
             'user': user,
             'username': username},
 'product_id': 2,
 'reviewed': {'birthday': None,
              'confirmed': False,
              'email': 'killer23@gmail.com',
              'is_admin': 0,
              'name': None,
              'surname': None,
              'username': 'the killer god'},
 'reviewer': {'birthday': None,
              'confirmed': True,
              'email': 'pepe432@gmail.com',
              'is_admin': 0,
              'name': None,
              'surname': None,
              'username': 'pepeman'},
 'stars': 4}


def test_get_all(_app, dummy_review):
    with _app.app_context():
        result = len(ReviewsModel.get_all())
        assert result == 1


def test_get_reviews_by_email(_app, dummy_review):
    with _app.app_context():
        result = ReviewsModel.get_reviews_by_email("pepe432@gmail.com")
        assert len(result) == 0
        result = ReviewsModel.get_reviews_by_email("killer23@gmail.com")
        assert len(result) == 1


def test_save_order(_app):
    with _app.app_context():
        previous = len(ReviewsModel.get_all())
        r = ReviewsModel("pepe432@gmail.com", "killer23@gmail.com", 2, 4, "")
        ReviewsModel.save_to_db(r)
        result = len(ReviewsModel.get_all())

        assert previous == 0
        assert result == 1


def test_delete_product(_app, dummy_review):
    with _app.app_context():
        previous = len(ReviewsModel.get_all())
        ReviewsModel.delete_from_db(dummy_review)
        result = len(ReviewsModel.get_all())

        assert previous == 1
        assert result == 0




