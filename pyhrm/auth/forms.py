from flask_wtf.form import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

from pyhrm.user import User
from pyhrm.utils import PyHRMForm


class RegistrationForm(PyHRMForm):
    email = StringField('Email', [DataRequired(), Length(max=127)])
    username = StringField('Username', [DataRequired(), Length(max=64)])
    password = PasswordField('Password', [DataRequired(), Length(max=32, min=6, message='Password must be at least 6 characters long and contains one special character')])
    confirm_password = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])
    first_name = StringField('First Name', [DataRequired(), Length(min=3)])
    middle_name = StringField('Middle Name')
    last_name = StringField('Last Name', [DataRequired(), Length(min=3)])
    accept_tos = BooleanField('I accept the Terms of Service', [DataRequired(message="You need to accept the terms of service in order to continue")], default=True)
    
    def validate(self, extra_validators=None):
        check_validate = super(RegistrationForm, self).validate()
        
        if not check_validate:
            return False
        
        user = User.query.filter_by(
            username=self.username,
            email=self.email
        )
        
        if user:
            return False
        
        return True
    

class LoginForm(PyHRMForm):
    principal = StringField('Username or email', [DataRequired()])
    credential = PasswordField('Password', [DataRequired()])
    
    def validate(self, extra_validators=None):
        check_validate = super(LoginForm, self).validate()
        
        if not check_validate:
            return False
        
        return True