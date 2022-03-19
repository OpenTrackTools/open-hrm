from api import User, Profile
from app import app, db


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Profile=Profile)
