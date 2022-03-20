from api import User, Profile
from webapp import db
from main import app


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Profile=Profile)
