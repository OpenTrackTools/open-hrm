from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from openhrmapp.models import User


class LoginForm(FlaskForm):
    login = StringField('Username or email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign in')

    def validate(self, extra_validators=None):
        return True


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo(fieldname='password_confirm',
                                                                             message='Password must match')])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Sign up')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already has been taken.')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already has been taken.')


class UpdateUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    profile_picture = FileField('Update Profile Picture', validators=[FileAllowed(['png', 'jpeg', 'jpg'])])
    submit = SubmitField('Update')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already has been taken.')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already has been taken.')
