from pyhrm.commons import Base
from pyhrm.commons import CRUDMixin
from pyhrm.ext import db


class Department(Base, CRUDMixin):
    __tablename__ = 'departments'
    
    name = db.Column("name", db.String(255), nullable=False, unique=True)
    description = db.Column("description", db.String(255))
    short_code = db.Column("short_code", db.String(16), nullable=False, unique=True)
    hod = db.Column("hod", db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    owner = db.Column("dept_owner", db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    parent_dept = db.Column("parent_dept", db.Integer, db.ForeignKey('departments.id', ondelete='CASCADE'), nullable=False, default=-1)
    is_dissolved = db.Column("is_dissolved", db.Boolean, default=False)
    dissolved_reason = db.Column("dissolved_reason", db.String(255))
    dissolved_by = db.Column("dissolved_by", db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    dissolved_at = db.Column("dissolved_at", db.DateTime(timezone=False))
    