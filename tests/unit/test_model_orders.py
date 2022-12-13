import datetime
from models.orders import OrdersModel


def test_create_order():
    o = OrdersModel("pepe432@gmail.com", "killer23@gmail.com", 2, 1234567890, 123, "Pepe", "05-05-2025")

    assert o.buyer_id == "pepe432@gmail.com"
    assert o.seller_id == "killer23@gmail.com"
    assert o.product_id == 2
    assert o.credit_card == 1234567890
    assert o.cvc == 123
    assert o.cc_owner == "Pepe"
    assert o.cc_expiration_date == "05-05-2025"


def test_json(_app, dummy_order):
    with _app.app_context():
        current_date = datetime.date.today()
        user = dummy_order.json()['product']['user']
        username = dummy_order.json()['product']['username']
        expected = {'buyer': {'birthday': None,
                              'confirmed': True,
                              'email': 'pepe432@gmail.com',
                              'is_admin': 0,
                              'name': None,
                              'surname': None,
                              'username': 'pepeman',
                              'profile': 'https://storage.googleapis.com/wallapopo-img/default-profile.jpg'},
                    'cc_expiration_date': '03/25',
                    'cc_owner': 'Pepe',
                    'credit_card': 1234567890,
                    'cvc': 123,
                    'date': current_date.strftime('%d-%m-%Y'),
                    'id': 1,
                    'product': {'category': 'Otros',
                                'condition': 'Casi nuevo',
                                'date': current_date.strftime("%d-%b-%Y"),
                                'description': 'juego de parchis edición retro',
                                'id': 2,
                                'image': ['Parchis.jpeg'],
                                'name': 'Parchis',
                                'price': 20.0,
                                'shipment': False,
                                'status': 'En venta',
                                'user': user,
                                'username': username
                                },
                    'product_id': 2,
                    'seller': {'birthday': None,
                               'confirmed': False,
                               'email': 'killer23@gmail.com',
                               'is_admin': 0,
                               'name': None,
                               'surname': None,
                               'username': 'the killer god',
                               'profile': 'https://storage.googleapis.com/wallapopo-img/default-profile.jpg'}}
        assert dummy_order.json() == expected


def test_get_all(_app, dummy_order):
    with _app.app_context():
        result = len(OrdersModel.get_all())
        assert result == 1


def test_get_purchases_by_email(_app, dummy_order):
    with _app.app_context():
        result = OrdersModel.get_purchases_by_email("pepe432@gmail.com")
        assert len(result) == 1


def test_get_sales_by_email(_app, dummy_order):
    with _app.app_context():
        email = dummy_order.json()['seller']['email']
        result = OrdersModel.get_sales_by_email(email)
        assert len(result) == 1


def test_save_order(_app):
    with _app.app_context():
        previous = len(OrdersModel.get_all())
        o = OrdersModel("pepe432@gmail.com", "killer23@gmail.com", 2, 1234567890, 123, "Pepe",
                        datetime.datetime(2025, 3, 3, 10, 10, 10))
        OrdersModel.save_to_db(o)
        result = len(OrdersModel.get_all())

        assert previous == 0
        assert result == 1


def test_delete_product(_app, dummy_order):
    with _app.app_context():
        previous = len(OrdersModel.get_all())
        OrdersModel.delete_from_db(dummy_order)
        result = len(OrdersModel.get_all())

        assert previous == 1
        assert result == 0




