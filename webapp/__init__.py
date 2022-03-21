from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_assets import Environment, Bundle
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
asset_env = Environment()
csrf = CSRFProtect()

# TODO will be changed once the client application finalized

main_css = Bundle(
    'css/bootstrap.css',
    filters='cssmin',
    output='css/app.min.css'
)

main_js = Bundle(
    'js/jquery.js',
    'js/bootstrap.js',
    filters='jsmin',
    output='js/app.min.js'
)


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)
    db.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)
    
    asset_env.register('js_all', main_js)
    asset_env.register('css_all', main_css)
    asset_env.init_app(app)
    
    from .authentication import create_module as auth_create_mod
    from .validation import create_module as validation_create_mod
    from .app import create_module as app_create_mod
    
    auth_create_mod(app)
    validation_create_mod(app)
    app_create_mod(app)
    
    return app
