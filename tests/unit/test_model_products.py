import datetime
from models.products import ProductsModel


def test_create_product():
    p = ProductsModel("Nintendo Switch", "Consolas y Videojuegos", "Apenas la uso y necesito dinero", 150, "Casi nuevo")

    assert p.name == "Nintendo Switch"
    assert p.category == "Consolas y Videojuegos"
    assert p.description == "Apenas la uso y necesito dinero"
    assert p.price == 150
    assert p.condition == "Casi nuevo"


def test_json(_app, switch_product):
    with _app.app_context():
        date = datetime.datetime.now()
        switch_product.date = date
        expected = {
                    'category': 'Consolas y Videojuegos',
                    'condition': 'Casi nuevo',
                    'date': date.date().strftime("%d-%b-%Y"),
                    'description': 'Apenas la uso y necesito dinero',
                    'id': 99,
                    'image': None,
                    'name': 'Nintendo Switch',
                    'price': 150,
                    'shipment': None,
                    'status': None,
                    'user': 'pepe432@gmail.com',
                    'username': 'pepeman',
                    'user_image': 'https://storage.googleapis.com/wallapopo-img/default-profile.jpg'
                    }
        assert switch_product.json() == expected


def test_get_all(_app):
    with _app.app_context():
        result = len(ProductsModel.get_all())
        assert result == 4


def test_get_all_by_user(_app, pepe_products):
    with _app.app_context():
        result = ProductsModel.get_all_by_user("pepe432@gmail.com")
        assert len(result) == len(pepe_products)


def test_get_by_id(_app):
    with _app.app_context():
        result = ProductsModel.get_by_id(1)

        assert str(result) == "<ProductsModel 1>"


def test_save_product(_app, switch_product):
    with _app.app_context():
        previous = len(ProductsModel.get_all())
        ProductsModel.save_to_db(switch_product)
        result = len(ProductsModel.get_all())

        assert previous == 4
        assert result == 5


def test_delete_product(_app):
    with _app.app_context():
        previous = len(ProductsModel.get_all())
        user = ProductsModel.get_by_id(1)
        ProductsModel.delete_from_db(user)
        result = len(ProductsModel.get_all())

        assert previous == 4
        assert result == 3




