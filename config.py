class Config(object):
    SECRET_KEY = '9b755692e0a99a14183d46f6ce7ef16666aab1362f7a89e16802c453128323ea'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://phadmin:phpass@localhost:5432/pyhrm"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
