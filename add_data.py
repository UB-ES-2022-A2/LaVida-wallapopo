from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# import models here
from models.products import ProductsModel
from models.accounts import AccountsModel
import resources.sample_data as data

import random as rand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

products = []
accounts = []

for product in data.products:
    productModel = ProductsModel(name=product['name'], category=product['category'], description=product['description'],
                                 price=product['price'])
    products.append(productModel)

for account in data.accounts:
    accountModel = AccountsModel(email=account['user_id'])
    accounts.append(accountModel)

for product in products:
    user = rand.choice(accounts)
    product.user_id = user

    if accounts[accounts.index(user)] == user:
        accounts[accounts.index(user)].products = product

db.session.add_all(products)
db.session.add_all(accounts)
db.session.commit()
