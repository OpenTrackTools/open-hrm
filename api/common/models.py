import datetime

from webapp import db
import uuid


class Base(db.Model):
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    object_id = db.Column("object_id", db.String(255), unique=True, nullable=False)
    created_by = db.Column("created_by", db.Integer, nullable=False, default=-1)
    created_at = db.Column("created_at", db.DateTime(timezone=False), nullable=False, default=db.func.now())
    updated_at = db.Column("updated_at", db.DateTime(timezone=False))
    updated_by = db.Column("updated_by", db.Integer, default=-1)
    deleted = db.Column("is_deleted", db.Boolean, default=False)
    deleted_by = db.Column("deleted_by", db.Integer, default=-1)
    deleted_at = db.Column("deleted_at", db.DateTime(timezone=False))
    
    def __init__(self):
        self.object_id = uuid.uuid4()