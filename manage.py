from main import app
from pyhrm.ext import db
from pyhrm.user import User, Profile
from pyhrm.dept import Department


@app.shell_context_processor
def shell_ctx():
    return dict(app=app, db=db,
                User=User,
                Profile=Profile,
                Department=Department
                )
