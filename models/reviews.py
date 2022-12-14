from db import db
from sqlalchemy.sql import func

from models.accounts import AccountsModel
from models.products import ProductsModel


class ReviewsModel(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    reviewer_id = db.Column(db.String(50), db.ForeignKey('accounts.email'), nullable=False)
    reviewed_id = db.Column(db.String(50), db.ForeignKey('accounts.email'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(500), nullable=True)
    # the date when review was done
    date = db.Column(db.DateTime(), nullable=False, server_default=func.now())

    def __init__(self, reviewer_id, reviewed_id, product_id, stars, comment):
        self.reviewer_id = reviewer_id
        self.reviewed_id = reviewed_id
        self.product_id = product_id
        self.stars = stars
        self.comment = comment

    def json(self):
        return {
            'id': self.id,
            'reviewer': AccountsModel.get_by_email(self.reviewer_id).json(),
            'reviewed': AccountsModel.get_by_email(self.reviewed_id).json(),
            'product_id': self.product_id,
            'product': ProductsModel.get_by_id(self.product_id).json(),
            'stars': self.stars,
            'comment': self.comment,
            'date': self.date.strftime('%Y-%m-%d')
        }

    @classmethod
    def get_all(cls):  # returns all orders
        return cls.query.all()

    @classmethod
    def get_reviews_by_email(cls, email):  # returns all reviews by email
        return cls.query.filter_by(reviewed_id=email).all()

    @classmethod
    def get_by_id(cls, id):  # returns review by id
        return cls.query.get(id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
