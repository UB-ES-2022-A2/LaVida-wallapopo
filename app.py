from flask import Flask
from flask_migrate import Migrate
from db import db
from models.accounts import AccountsModel
from models.products import ProductsModel

app = Flask(__name__)

# config used for now, will be changed later on
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
