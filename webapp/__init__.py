from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .authentication import create_module as auth_create_mod
    auth_create_mod(app)
    return app
