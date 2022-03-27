from pyhrm.ext import db
import uuid


class Base(db.Model):
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    _object_id = db.Column("object_id", db.String(255), unique=True, nullable=False)
    created_by = db.Column("created_by", db.Integer, nullable=False, default=-1)
    created_at = db.Column("created_at", db.DateTime(timezone=False), nullable=False, default=db.func.now())
    updated_at = db.Column("updated_at", db.DateTime(timezone=False))
    updated_by = db.Column("updated_by", db.Integer, default=-1)
    deleted = db.Column("is_deleted", db.Boolean, default=False)
    deleted_by = db.Column("deleted_by", db.Integer, default=-1)
    deleted_at = db.Column("deleted_at", db.DateTime(timezone=False))
    
    def __init__(self):
        self._object_id = uuid.uuid4()
    
    @property
    def object_id(self):
        return self._object_id
    

class Organization(Base):
    __tablename__ = 'organizations'
    
    name = db.Column("name", db.String(255), nullable=False, unique=True)
    description = db.Column("description", db.String(1000))
    owner = db.Column("owner", db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False, default=-1)
    email_domain = db.Column("email_domain", db.String(255), unique=True)
    logo_path = db.Column("logo_path", db.String(255), unique=True, nullable=False, default='assets/logo/default.png')
    
    def __init__(self, name):
        super().__init__()
        self.name = name
    
  
class Branch(Base):
    __tablename__ = 'branches'
    
    name = db.Column("name", db.String(255), unique=True, nullable=False)
    code = db.Column("code", db.String(128), unique=True, nullable=False)
    description = db.Column("description", db.String(1024))
    contact = db.Column("contact", db.String(255), unique=True)
    secondary_contact = db.Column("secondary_contact", db.String(255))
    email = db.Column("email", db.String(255), unique=True)
    contact_address_line_1 = db.Column("address_1", db.String(512), nullable=False)
    contact_address_line_2 = db.Column("address_2", db.String(512))
    zip_id = db.Column("zip_id", db.Integer)
    state_id = db.Column("state_id", db.Integer)
    country_id = db.Column("country_id", db.Integer)
    is_main = db.Column("is_main", db.Boolean, default=False)
    
    def __init__(self, name, code):
        super().__init__()
        self.name = name
        self.code = code
    