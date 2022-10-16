from db import db
from sqlalchemy.sql import func

# possible categories, we can modify its content if needed
categories_list = ('Coches', 'Motos', 'Motor y Accesorios', 'Moda y Accesorios', 'TV, Audio y Foto',
                   'Móviles y Telefonía', 'Informática y Electrónica', 'Deporte y Ocio', 'Bicicletas',
                   'Consolas y Videojuegos', 'Hogar y Jardín', 'Electrodomésticos', 'Cine', 'Libros y Música',
                   'Niños y Bebés', 'Coleccionismo', 'Construcción y Reformas', 'Industria y Agricultura', 'Otros')

# product status, it checks if the product is for sale, reserved or sold
status_list = ('On sale', 'Reserved', 'Sold')


class ProductsModel(db.Model):
    __tablename__ = 'products'  # This is table name

    # basic product informations
    id = db.Column(db.Integer, primary_key=True)  # primary key
    name = db.Column(db.String(50), nullable=False)  # string with a max length of 50
    # one product can have multiple images
    image = db.Column(db.String(), nullable=True)  # only one image for now
    # validate_string=True raises an error if the value is not inside enum
    category = db.Column(db.Enum(*categories_list, name='categories_types', validate_strings=True), nullable=False)
    # by default, products are listed as selling
    status = db.Column(db.Enum(*status_list, name='status_types', validate_strings=True),
                       nullable=False, server_default=status_list[0])
    # description has a max length of 1000 characters
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Float, nullable=False)
    # the date when product was created
    date = db.Column(db.DateTime(), nullable=False, server_default=func.now())

    # foreign keys
    user_id = db.Column(db.String(), db.ForeignKey('accounts.email'))

    def __init__(self, name, category, description, price):
        self.name = name
        self.category = category
        self.description = description
        self.price = price

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'description': self.description,
            'price': self.price,
            'image': self.image,
            'status': self.status,
            'date': self.date,
            'user': self.user_id
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all_by_user(cls, email): # returns all products owned by account
        return cls.query.filter(cls.user_id == email).all()

    @classmethod
    def get_by_id(cls, id):  # returns product by id
        return cls.query.get(id)

    @classmethod
    def get_all(cls):
        return cls.query.all()