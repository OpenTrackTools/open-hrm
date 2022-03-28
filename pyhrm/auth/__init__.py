from flask_bcrypt import Bcrypt
from flask_login import LoginManager

bcrypt = Bcrypt()
login_manager = LoginManager()


def create_module(app, **kwargs):
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    from .controller import auth
    app.register_blueprint(auth)
    
    
@login_manager.user_loader
def load_user(user_id):
    from pyhrm.user import User
    return User.query.get(user_id)

