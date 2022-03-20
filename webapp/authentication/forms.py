from api.authentication.models import User
from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(Form):
    email = StringField('Email', [DataRequired(), Length(max=255)])
    username = StringField('Username', [DataRequired(), Length(max=255)])
    password = PasswordField('Password', [DataRequired(), Length(min=6, max=18)])
    confirm = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])
    
    def validate(self, extra_validators=None):
        check_validate = super(RegistrationForm, self).validate()
        
        if not check_validate:
            return False
        
        user = User.query.filter_by(
            username=self.username.data,
            email=self.email.data
        ).first()
        
        if user:
            return False
        
        return True
    