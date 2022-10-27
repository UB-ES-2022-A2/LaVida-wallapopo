import random as rand

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import resources.sample_data as data
from models.accounts import AccountsModel
# import models here
from models.products import ProductsModel

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
    productModel.image = product['image']
    productModel.status = product['status']
    products.append(productModel)

for account in data.accounts:
    accountModel = AccountsModel(email=account['email'], username=account['username'])
    accountModel.hash_password(account['password'])

    accounts.append(accountModel)

# Relationship between products and user
for product in products:
    user = rand.choice(accounts)
    i = accounts.index(user)
    product.user_id = accounts[i].email

db.session.add_all(products)
db.session.add_all(accounts)
db.session.commit()
