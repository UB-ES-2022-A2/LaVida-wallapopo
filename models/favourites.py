from db import db
from models.accounts import AccountsModel
from sqlalchemy.sql import func, desc


class FavouritesModel(db.Model):
    __tablename__ = 'favourites'  # This is the table name

    # favourite product basic information
    id = db.Column(db.Integer, primary_key=True)  # primary key
    name = db.Column(db.String(50), nullable=False)  # string with a max length of 50
    liked = db.Column(db.Boolean, nullable=False, server_default=False)  # or "0" boolean that indicates if prod is fav
    # or not

    # foreign keys
    user_id = db.Column(db.String(50), db.ForeignKey('accounts.email'))

    def __init__(self, name, liked):
        self.name = name
        self.liked = liked

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'liked': self.liked,
            'user': self.user_id,
            'username': AccountsModel.get_by_email(self.user_id).json()['username'],
        }

    """def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()"""


    @classmethod
    def get_by_id(cls, id):
        return cls.query().get(id)


    @classmethod
    def get_products_by_fav(cls):
        query = cls.query()
        if cls.liked:
            query = query.filter(cls.liked).all()

        return query

