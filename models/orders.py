from db import db
from sqlalchemy.sql import func, desc


class OrdersModel(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.String(50), db.ForeignKey('accounts.email'), nullable=False)
    seller_id = db.Column(db.String(50), db.ForeignKey('accounts.email'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    credit_card = db.Column(db.Integer, nullable=False)
    cvc = db.Column(db.Integer, nullable=False)
    cc_expiration_date = db.Column(db.Date(), nullable=True)
    cc_owner = db.Column(db.String(50), nullable=False)
    # the date when order was created
    date = db.Column(db.DateTime(), nullable=False, server_default=func.now())

    # relationship account 1-* orders
    buyer = db.relationship("AccountsModel", foreign_keys=[buyer_id])
    seller = db.relationship("AccountsModel", foreign_keys=[seller_id])
    product = db.relationship("ProductsModel", foreign_keys=[product_id])

    def __init__(self, buyer_id, seller_id, product_id, cc, cvc, cc_owner, cc_exp):
        self.buyer_id = buyer_id
        self.seller_id = seller_id
        self.product_id = product_id
        self.credit_card = cc
        self.cvc = cvc
        self.cc_expiration_date = cc_exp
        self.cc_owner = cc_owner

    def json(self):
        return {
            'id': self.id,
            'buyer': self.buyer.json(),
            'seller': self.seller.json(),
            'product_id': self.product_id,
            'product': self.product.json(),
            'credit_card': self.credit_card,
            'cc_owner': self.cc_owner,
            'cvc': self.cvc,
            'cc_expiration_date': self.cc_expiration_date.strftime('%m/%y'),
            'date': self.date.strftime('%d-%m-%Y')
        }

    @classmethod
    def get_all(cls):  # returns all orders
        return cls.query.all()

    @classmethod
    def get_purchases_by_email(cls, email):  # returns all orders by email
        query = cls.query.filter_by(buyer_id=email)
        return query.order_by(desc(cls.date)).all()

    @classmethod
    def get_sales_by_email(cls, email):  # returns all products sold by email
        query = cls.query.filter_by(seller_id=email)
        return query.order_by(desc(cls.date)).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
