from db import db

from models.accounts import AccountsModel
from models.products import ProductsModel


class FavouritesModel(db.Model):
    __tablename__ = 'favourites'  # This is the table name

    # favourite product basic information
    id = db.Column(db.Integer, primary_key=True)  # primary key

    # foreign keys
    user_id = db.Column(db.String(50), db.ForeignKey('accounts.email'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    def __init__(self, user_id, product_id):
        self.user_id = user_id
        self.product_id = product_id

    def json(self):
        return {
            'id': self.id,
            'user': AccountsModel.get_by_email(self.user_id).json(),
            'product': ProductsModel.get_by_id(self.product_id).json()
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_email(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    @classmethod
    def get_fav(cls, user_id, product_id):
        query = cls.query.filter(cls.user_id == user_id)
        return query.filter(cls.product_id == product_id).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()
