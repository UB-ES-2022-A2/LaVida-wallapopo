from flask import Flask
from flask_migrate import Migrate
from db import db, secret_key
from flask_cors import CORS
from flask_restful import Api
from flask import render_template

from models.accounts import AccountsModel
from models.products import ProductsModel
from resources.accounts import Accounts
from resources.products import ProductsList
from resources.login import Login


app = Flask(
    __name__,
    static_folder="./frontend/dist/static",
    template_folder="./frontend/dist"
)

api = Api(app)
CORS(app, resources={r'/*': {'origins': '*'}})

# config used for now, will be changed later on
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secret_key

migrate = Migrate(app, db)
db.init_app(app)

# accounts
api.add_resource(Accounts, '/account/<string:email>', '/account')

# products
api.add_resource(ProductsList, '/products')

# login
api.add_resource(Login, '/login')


@app.route('/')
def render_vue():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=5000, debug=True)
