from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_login import LoginManager

bcrypt = Bcrypt()
jwt = JWTManager()

login_manager = LoginManager()


def create_module(app, **kwargs):
    bcrypt.init_app(app)
    login_manager.init_app(app)
    jwt.init_app(app)
    
    from .controllers import auth_bp
    app.register_blueprint(auth_bp)


@login_manager.user_loader
def load_user(userid):
    from api.authentication.models import User
    return User.query.get(userid)
