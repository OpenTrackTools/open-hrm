from api.common.models import Base
from webapp import db

import uuid


class User(db.Model, Base):
    __tablename__ = 'users'
    
    username = db.Column("username", db.String(255), unique=True, nullable=False)
    email = db.Column("email", db.String(255), unique=True, nullable=False)
    password = db.Column("password", db.String(255), nullable=False)
    # profile = db.relationship("profile", back_populates='users', lazy=True, uselist=False)
    
    def __init__(self, username):
        self.object_id = uuid.uuid4()
        self.username = username
    
    def __repr__(self):
        return "<User '{}' '{}'>".format(self.object_id, self.username)


class Profile(db.Model, Base):
    __tablename__ = 'user_profiles'
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # Basic profile details
    first_name = db.Column("first_name", db.String(255))
    middle_name = db.Column("middle_name", db.String(255))
    last_name = db.Column("last_name", db.String(255))
    emp_id = db.Column("employee_id", db.String(255))
    display_name = db.Column("display_name", db.String(255))
    avatar = db.Column("avatar", db.String(255))
    
    # Address details
    contact_address_line_1 = db.Column("contact_address_line_1", db.String(255))
    contact_address_line_2 = db.Column("contact_address_line_2", db.String(255))
    # Zip code, state and country will be loaded from external data
    # based on the selected country/continent/province
    zip_id = db.Column("zip_id", db.Integer)
    state_id = db.Column("state_id", db.Integer)
    country_id = db.Column("country_id", db.Integer)
    
    # Roles, designation and relations
    role_id = db.Column("role_id", db.Integer)
    designation_id = db.Column("designation_id", db.Integer)
    reports_to = db.Column("reports_to", db.Integer)
    
    # public profile
    short_url = db.Column("short_url", db.String(255))