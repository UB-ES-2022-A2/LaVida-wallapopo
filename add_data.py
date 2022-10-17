from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# import models here
from models.products import ProductsModel
import resources.sample_data as data

import random as rand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

products = []

for product in data.products:
    productModel = ProductsModel(id=product['id'], name=product['name'], image=product['image'],
                                 category=product['category'], status=product['status'], description=product['description'],
                                 price=product['price'], date=product['date'], user=product['user_id'])
    products.append(productModel)

# TODO Relationships in next sprints(prod-user).

db.session.add_all(products)
db.session.commit()
