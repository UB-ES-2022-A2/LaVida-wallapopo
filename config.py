from decouple import config
import os


class Config:
    pass


class ProductionConfig(Config):
    # Get environment variables defined in app.yaml
    db_user = os.environ.get('CLOUD_SQL_USERNAME')
    db_password = os.environ.get('CLOUD_SQL_PASSWORD')
    db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
    db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://{user}:{password}@localhost/{database}'
        '?unix_socket=/cloudsql/{connection_name}').format(
        user=db_user, password=db_password,
        database=db_name, connection_name=db_connection_name)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = "/static"
    TEMPLATE_FOLDER = "/templates"
    SECRET_KEY = config('SECRET_KEY', default='localhost')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    """
    # Si no acabase de ir con sqlite cambiar a esto y preguntar a MarcS como usarlo
    SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://{user}:{password}@localhost/{database}').format(
        user=db_user, password=db_password,
        database=db_name)
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = "/frontend/dist/static"
    TEMPLATE_FOLDER = "/frontend/dist"
    SECRET_KEY = "kdsfklsmfakfmafmadslvsdfasdf"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = "/frontend/dist/static"
    TEMPLATE_FOLDER = "/frontend/dist"
    SECRET_KEY = "kdsfklsmfakfmafmadslvsdfasdf"


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
