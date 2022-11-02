import pytest

import datetime
from app import app
from models.products import ProductsModel


def test_create_product():
    p = ProductsModel("Nintendo Switch", "Consolas y Videojuegos", "Apenas la uso y necesito dinero", 150, "Casi nuevo")

    assert p.name == "Nintendo Switch"
    assert p.category == "Consolas y Videojuegos"
    assert p.description == "Apenas la uso y necesito dinero"
    assert p.price == 150
    assert p.condition == "Casi nuevo"


def test_json(switch_product):
    date = datetime.datetime.now()
    switch_product.date = date
    expected = {
                'category': 'Consolas y Videojuegos',
                'condition': 'Casi nuevo',
                'date': date.isoformat(),
                'description': 'Apenas la uso y necesito dinero',
                'id': None,
                'image': None,
                'name': 'Nintendo Switch',
                'price': 150,
                'status': None,
                'user': None
                }
    assert switch_product.json() == expected


def test_get_all():
    with app.app_context():
        result = len(ProductsModel.get_all())
        assert result == 4

"""
def test_get_all_by_user(pepe_products):
    with app.app_context():
        result = ProductsModel.get_all_by_user("pepe432@gmail.com")

        assert len(result) == len(pepe_products)
"""

def test_get_by_id():
    with app.app_context():
        result = ProductsModel.get_by_id(1)

        assert str(result) == "<ProductsModel 1>"


def test_save_product(switch_product):
    with app.app_context():
        previous = len(ProductsModel.get_all())
        ProductsModel.save_to_db(switch_product)
        result = len(ProductsModel.get_all())

        assert previous == 4
        assert result == 5


def test_delete_product():
    with app.app_context():
        previous = len(ProductsModel.get_all())
        user = ProductsModel.get_by_id(5)
        ProductsModel.delete_from_db(user)
        result = len(ProductsModel.get_all())

        assert previous == 5
        assert result == 4




