from flask_caching import Cache
from flask_migrate import Migrate
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

metadata = MetaData(
    naming_convention= {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

db = SQLAlchemy(metadata==metadata, session_options={"future": True})
login_manager = LoginManager()
mail = Mail()
cache = Cache()
csrf = CSRFProtect()
bcrypt = Bcrypt()
migrate = Migrate()
