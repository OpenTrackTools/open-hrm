from flask import Flask

from pyhrm.ext import db, csrf, mail, cache, migrate


def create_app(config_path=None, app_path=None):
    app = Flask(__name__, instance_path=app_path, instance_relative_config=True)
    configure_app(app, config_path)
    configure_extension(app)


def configure_app(app, config_path):
    app.config.from_object(__name__)
    if config_path is not None:
        # Load the provided config and override the
        # default settings
        pass


def configure_extension(app):
    db.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)
    cache.init_app(app)
    migrate.init_app(app)
    