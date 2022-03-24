from pyhrm.commons import Base
from pyhrm.ext import db, bcrypt
from pyhrm.utils import CRUDMixin


class User(Base, CRUDMixin):
    __tablename__ = 'users'
    
    username = db.Column("username", db.String(255), unique=True, nullable=False)
    email = db.Column("email", db.String(255), unique=True, nullable=False)
    password = db.Column("password", db.String(255), nullable=False)
    is_active = db.Column("is_active", db.Boolean, nullable=False, default=True)

    def __init__(self, email, username, password):
        super().__init__()
        self.authenticated = None
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password=password).decode('utf8')


class Profile(Base):
    __tablename__ = 'profiles'
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    # Basic profile details
    first_name = db.Column("first_name", db.String(255))
    middle_name = db.Column("middle_name", db.String(255))
    last_name = db.Column("last_name", db.String(255))
    emp_id = db.Column("employee_id", db.String(255))
    display_name = db.Column("display_name", db.String(255))
    date_of_birth = db.Column("date_of_birth", db.DateTime(timezone=False), nullable=False)
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
    
    def __init__(self):
        super().__init__()
        