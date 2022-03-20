from flask import (
    render_template,
    Blueprint
)

from api import User
from .forms import RegistrationForm
from webapp.authentication import bcrypt
from webapp import db

auth_bp = Blueprint(
    'auth',
    __name__,
    template_folder='../templates/auth',
    url_prefix="/auth"
)


@auth_bp.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data)
        new_user = User(form.email.data, form.username.data, pw_hash)
        db.session.add(new_user)
        db.session.commit()
    
    return render_template('register.html', form=form, title="Registration - PyHRM")
