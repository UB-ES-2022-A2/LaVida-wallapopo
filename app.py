import os

from flask import Flask
from flask import render_template
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from config import config
from db import db
from resources.accounts import Accounts
from resources.products import Product, ProductsList
from resources.session import Login, Logout

app = Flask(__name__)
# Set default environment as developement
environment = config['development']

# If it's deployed change environment to production
if os.environ.get('GAE_ENV') == 'standard':
    environment = config['production']

app.config.from_object(environment)

api = Api(app)
CORS(app, resources={r'/*': {'origins': '*'}})

migrate = Migrate(app, db)
db.init_app(app)

# accounts
api.add_resource(Accounts, '/account/<string:email>', '/account')

# products
api.add_resource(Product, '/product/<string:id>')
api.add_resource(ProductsList, '/products')

# session
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout/<string:email>')


@app.route('/')
def render_vue():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=5000, debug=True)
