from pyhrm.commons import Base
from pyhrm.ext import db, bcrypt


class User(Base):
    __tablename__ = 'users'
    
    username = db.Column("username", db.String(255), unique=True, nullable=False)
    email = db.Column("email", db.String(255), unique=True, nullable=False)
    password = db.Column("password", db.String(255), nullable=False)
    is_active = db.Column("is_active", db.Boolean, nullable=False, default=True)
    reports_to = db.Column("reports_to", db.Integer, nullable=False, default=-1)
    department_id = db.Column("dept_id", db.Integer, db.ForeignKey('departments.id', ondelete='CASCADE'), nullable=False, default=-1)
    role_id = db.Column("role_id", db.Integer)
    designation_id = db.Column("designation_id", db.Integer, db.ForeignKey('designations.id', ondelete='CASCADE'), nullable=False, default=-1)

    def __init__(self, email, username, password):
        super().__init__()
        self.authenticated = None
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password=password).decode('utf8')

    def check_password(self, password):
        return bcrypt.check_password_hash(pw_hash=self.password, password=password)
    

class Profile(Base):
    __tablename__ = 'profiles'
    
    user_id = db.Column("user_id", db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
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
    
    # public profile
    short_url = db.Column("short_url", db.String(255))
    
    def __init__(self):
        super().__init__()
    
    
class Designation(Base):
    __tablename__ = 'designations'
    
    name = db.Column("name", db.String(255), unique=True, nullable=False)
    description = db.Column("description", db.String(255))
    short_code = db.Column("short_code", db.String(255), unique=True, nullable=False)
    
    def __init__(self, name, short_code, description=None):
        super().__init__()
        self.name = name
        self.short_code = short_code
        self.description = description


class Role(Base):
    __tablename__ = 'roles'

    name = db.Column("name", db.String(255), unique=True, nullable=False)
    description = db.Column("description", db.String(255))
    short_code = db.Column("short_code", db.String(255), unique=True, nullable=False)

    def __init__(self, name, short_code, description=None):
        super().__init__()
        self.name = name
        self.short_code = short_code
        self.description = description
        