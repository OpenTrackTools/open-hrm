class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = "postgresql://phadmin:phpass@localhost:5432/pyhrm"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
