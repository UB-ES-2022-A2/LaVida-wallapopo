import os

from flask import Flask
from flask import render_template
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from config import config
from db import db
from resources.accounts import Accounts
from resources.products import Product, ProductsList, AddProduct
from resources.session import Login, Logout
from resources.filters import Filter, FilterCategory
from resources.validate import Validate
from resources.profile import Profile

app = Flask(__name__)


# app = Flask(
#     __name__,
#     static_folder="frontend/dist/static",
#     template_folder="frontend/dist"
# )

# Set default environment as development, change to 'testing' before running tests
environment = config['development']
# testing CIss0

# If it's deployed change environment to production
if os.environ.get('GAE_ENV') == 'standard':
    environment = config['production']

app.config.from_object(environment)
app.config['SECURITY_PASSWORD_SALT'] = 'foobar'

api = Api(app)
CORS(app, resources={r'/*': {'origins': '*'}})

migrate = Migrate(app, db)
db.init_app(app)

# accounts
api.add_resource(Accounts, '/API/account/<string:email>', '/API/account')
api.add_resource(Validate, '/API/validation/<string:validation_token>', '/API/validation')
api.add_resource(Profile, '/API/profile/<string:email>', '/API/profile')

# products
api.add_resource(Product, '/API/product/<string:id>')
api.add_resource(ProductsList, '/API/products')
api.add_resource(AddProduct, '/API/catalog/add/<string:email>')

# filtering
api.add_resource(Filter, '/API/filter', '/API/filter/<string:text>')
api.add_resource(FilterCategory, '/API/category/<string:category>')

# session
api.add_resource(Login, '/API/login')
api.add_resource(Logout, '/API/logout/<string:email>')


@app.route('/')
def render_vue():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=5000, debug=True)
