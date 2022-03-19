from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

import uuid

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)


class Base(object):
    id = db.Column(db.Integer, primary_key=True)
    object_id = db.Column("object_id", db.String(255), unique=True, nullable=False)
    created_by = db.Column("created_by", db.Integer, nullable=False)
    created_at = db.Column("created_at", db.DateTime(timezone=False))
    updated_at = db.Column("updated_at", db.DateTime(timezone=False))
    updated_by = db.Column("updated_by", db.Integer, default=-1)
    deleted = db.Column("is_deleted", db.Boolean, default=False)
    deleted_by = db.Column("deleted_by", db.Integer, default=-1)
    deleted_at = db.Column("deleted_at", db.DateTime(timezone=False))
    

class User(db.Model, Base):
    
    __tablename__ = 'users'
    
    username = db.Column("username", db.String(255), unique=True, nullable=False)
    email = db.Column("email", db.String(255), unique=True, nullable=False)
    password = db.Column("password", db.String(255), nullable=False)
    
    def __init__(self, username):
        self.object_id = uuid.uuid4()
        self.username = username
        
    def __repr__(self):
        return "<User '{}' '{}'>".format(self.object_id, self.username)


@app.route('/')
def root():
    return "<h1>My beautiful pyhrm application</h1>"


if __name__ == "__main__":
    app.run(debug=True)
