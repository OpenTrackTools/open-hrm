from flask import url_for
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from werkzeug.utils import redirect

bcrypt = Bcrypt()
login_manager = LoginManager()


def create_module(app, **kwargs):
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    from .controllers import auth_bp
    app.register_blueprint(auth_bp)


def authenticate(login, password):
    from api import User
    
    if "@" not in login:
        # Assuming that username is given
        user = User.query.filter_by(username=login).first()
    else:
        user = User.query.filter_by(email=login).first()
        
    print(user)
    if not user:
        return None
    
    if not user.check_password(password):
        return None
    
    return user


@login_manager.user_loader
def load_user(userid):
    from api.authentication.models import User
    return User.query.get(userid)


@login_manager.unauthorized_handler
def unauthorized():
    """Redirects unauthorized user to the login page"""
    return redirect(url_for("auth.login"))
