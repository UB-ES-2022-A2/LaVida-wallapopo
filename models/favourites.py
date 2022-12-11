from db import db


class FavouritesModel(db.Model):
    __tablename__ = 'favourites'  # This is the table name

    # favourite product basic information
    id = db.Column(db.Integer, primary_key=True)  # primary key

    # foreign keys
    user_id = db.Column(db.String(50), db.ForeignKey('accounts.email'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    # relationships
    user = db.relationship("AccountsModel", foreign_keys=[user_id])
    product = db.relationship("ProductsModel", foreign_keys=[product_id])

    def __init__(self, user_id, product_id):
        self.user_id = user_id
        self.product_id = product_id

    def json(self):
        return {
            'id': self.id,
            'user': self.user.json(),
            'product': self.product.json()
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
    def get_all(cls):
        return cls.query.all()
