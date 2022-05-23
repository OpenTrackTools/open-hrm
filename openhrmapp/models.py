import uuid

from openhrmapp import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    object_id = db.Column("object_id", db.String(255), unique=True, nullable=False)
    created_by = db.Column("created_by", db.Integer, nullable=False, default=-1)
    created_at = db.Column("created_at", db.DateTime(timezone=False), nullable=False, default=datetime.utcnow())
    updated_at = db.Column("updated_at", db.DateTime(timezone=False))
    updated_by = db.Column("updated_by", db.Integer, default=-1)
    deleted = db.Column("is_deleted", db.Boolean, default=False)
    deleted_by = db.Column("deleted_by", db.Integer, default=-1)
    deleted_at = db.Column("deleted_at", db.DateTime(timezone=False))
    
    def __init__(self):
        self.object_id = uuid.uuid4()
    
    def get_id(self):
        return self.id


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(BaseModel, UserMixin):
    __tablename__ = 'users'
    
    profile_image = db.Column("profile_image", db.String(255), nullable=False, default='default_profile_image.png')
    email = db.Column("email", db.String(64), unique=True, index=True)
    username = db.Column("username", db.String(64), unique=True, index=True)
    password_encrypted = db.Column("password_encrypted", db.String(255))
    guest = db.Column("is_guest", db.Boolean, default=False)
    
    def __init__(self, email, username, password):
        super().__init__()
        self.email = email
        self.username = username
        self.password_encrypted = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_encrypted, password)
    
    def __repr__(self):
        return f"Username {self.username}"
