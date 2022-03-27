from main import app
from pyhrm.commons import Organization, Branch
from pyhrm.ext import db
from pyhrm.user import User, Profile, Designation
from pyhrm.dept import Department


@app.shell_context_processor
def shell_ctx():
    return dict(app=app, db=db,
                User=User,
                Profile=Profile,
                Designation=Designation,
                Organization = Organization,
                Branch = Branch,
                Department=Department
                )
