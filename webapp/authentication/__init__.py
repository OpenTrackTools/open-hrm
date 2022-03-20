from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from sqlalchemy import or_

bcrypt = Bcrypt()
login_manager = LoginManager()


def create_module(app, **kwargs):
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    from .controllers import auth_bp
    app.register_blueprint(auth_bp)


def authenticate(login, password):
    from api import User
    user = User.query.filter(or_(login == User.username, login == User.email)).first()
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
