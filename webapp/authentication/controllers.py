import flask
from flask import (
    render_template,
    Blueprint,
    request,
    redirect,
    url_for
)

from flask_login import login_user
from api import User
from .forms import RegistrationForm, LoginForm
from webapp.authentication import bcrypt, authenticate
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
        new_user = User(form.email.data, form.username.data, form.password.data)
        db.session.add(new_user)
        db.session.commit()
    
    return render_template('register.html', form=form, title="Registration - PyHRM")


@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = authenticate(form.login.data, form.password.data)
        if not user:
            form.login.errors.append('Invalid credential')
            return render_template('login.html', form=form, title="Login - PyHRM")
        else:
            login_user(user)
            next = request.args.get('next')
            return redirect(next or url_for("app.app"))

    return render_template('login.html', form=form, title="Login - PyHRM")