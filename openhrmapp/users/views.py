from flask import request, render_template, url_for, redirect, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from openhrmapp import db
from openhrmapp.models import User
from openhrmapp.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from openhrmapp.users.avatar_handler import add_profile_picture

users = Blueprint('users', __name__)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)
