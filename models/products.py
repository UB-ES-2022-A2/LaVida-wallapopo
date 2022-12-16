from db import db
from models.accounts import AccountsModel
from sqlalchemy.sql import func, desc

# possible categories, we can modify its content if needed
categories_list = ('Coches', 'Motos', 'Motor y Accesorios', 'Moda y Accesorios', 'TV, Audio y Foto',
                   'Móviles y Telefonía', 'Informática y Electrónica', 'Deporte y Ocio', 'Bicicletas',
                   'Consolas y Videojuegos', 'Hogar y Jardín', 'Electrodomésticos', 'Cine', 'Libros y Música',
                   'Niños y Bebés', 'Coleccionismo', 'Construcción y Reformas', 'Industria y Agricultura', 'Otros')

# product status, it checks if the product is for sale, reserved or sold
status_list = ('En venta', 'Reservado', 'Vendido')

# product condition, if it's new, almost new or used
condition_list = ('Nuevo', 'Casi nuevo', 'Usado')


class ProductsModel(db.Model):
    __tablename__ = 'products'  # This is table name

    # basic product information
    id = db.Column(db.Integer, primary_key=True)  # primary key
    name = db.Column(db.String(50), nullable=False)  # string with a max length of 50
    # validate_string=True raises an error if the value is not inside enum
    category = db.Column(db.Enum(*categories_list, name='categories_types', validate_strings=True), nullable=False)
    # by default, products are listed as selling
    status = db.Column(db.Enum(*status_list, name='status_types', validate_strings=True),
                       nullable=False, server_default=status_list[0])
    # if the product is new or not
    condition = db.Column(db.Enum(*condition_list, name='conditions_types', validate_strings=True),
                          nullable=False, server_default=condition_list[0])
    # description has a max length of 1000 characters
    description = db.Column(db.String(1000), nullable=False)
    shipment = db.Column(db.Boolean, nullable=False, server_default="0")
    price = db.Column(db.Float, nullable=False)
    # the date when product was created
    date = db.Column(db.DateTime(), nullable=False, server_default=func.now())

    # foreign keys
    user_id = db.Column(db.String(50), db.ForeignKey('accounts.email'))
    # one product can have multiple images
    _images = db.Column(db.String,
                        nullable=True,
                        server_default='https://storage.googleapis.com/wallapopo-img/product_placeholder.png'
                        )

    def get_images(self):
        return [x for x in self._images.split(';-;')] if self._images else None

    def images(self, value):
        if self._images == 'https://storage.googleapis.com/wallapopo-img/product_placeholder.png':
            self._images = value
        else:
            self._images += ';-;'+value

    def __init__(self, name, category, description, price, condition):
        self.name = name
        self.category = category
        self.description = description
        self.price = price
        self.condition = condition

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'description': self.description,
            'price': self.price,
            'image': self.get_images(),
            'condition': self.condition,
            'status': self.status,
            'date': self.date.date().strftime("%d-%b-%Y"),
            'user': self.user_id,
            'username': AccountsModel.get_by_email(self.user_id).json()['username'],
            'user_image': AccountsModel.get_by_email(self.user_id).json()['profile'],
            'shipment': self.shipment
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all_by_user(cls, email):  # returns all products owned by account
        return cls.query.filter(cls.user_id == email).all()

    @classmethod
    def get_by_id(cls, id):  # returns product by id
        return cls.query.get(id)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_filters(cls, cat, price0, price1, date, condition):
        # first retrieve all the products within the price range and condition
        query = cls.query
        # only return products from this category
        if cat is not None:
            query = query.filter(cls.category == cat)
        query = query.filter(
            (cls.price >= price0) &
            (cls.price <= price1) &
            cls.condition.in_(condition)
        )

        return query.order_by(desc(cls.date) if date else cls.date).all()

    @classmethod
    def get_by_search_text_filter(cls, text, cat, price0, price1, date, condition):
        # first retrieve all the products within the price range and condition
        query = cls.query
        # only return products from this category
        if cat is not None:
            query = query.filter(cls.category == cat)
        query = query.filter(
            (cls.price >= price0) &
            (cls.price <= price1) &
            cls.condition.in_(condition)
        )

        data = query.order_by(desc(cls.date) if date else cls.date)
        tag = "%{}%".format(text.lower())
        return data.filter(func.lower(cls.name).like(tag)).all()

    @classmethod
    def get_by_search_text(cls, text):
        tag = "%{}%".format(text.lower())
        return cls.query.filter(func.lower(cls.name).like(tag)).all()

    @classmethod
    def get_by_category(cls, category):
        return cls.query.filter_by(category=category).all()
