from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from pyhrm.user import User

bcrypt = Bcrypt()
login_manager = LoginManager()


def create_module(app, **kwargs):
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    from .controller import auth
    app.register_blueprint(auth)
    
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def authenticate(principal, credential):
    if '@' not in principal:
        # Assuming it is an username instead of email
        user = User.query.filter_by(username=principal).first()
    else:
        user = User.query.filter_by(email=principal).first()
    
    if not user:
        return None
    
    if not user.check_password(credential):
        return None
    
    return user
