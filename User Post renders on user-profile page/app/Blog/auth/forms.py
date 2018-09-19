from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from Blog.models import User



class RegistrationForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired(),Length(min=2,max=20)])
    username=StringField('Username',validators=[DataRequired(),Length(min=2, max=15)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit =SubmitField('Sign up')

    def validate_name(form,name):
        name=User.query.filter_by(name=form.name.data).first()
        if name:
            raise ValidationError('Name has already been taken.')

    def validate_email(form,email):
        email=User.query.filter_by(email=form.email.data).first()
        if email:
            raise ValidationError('Email has already been taken.')

    def validate_username(form,username):
        username=User.query.filter_by(username=form.username.data).first()
        if username:
                raise ValidationError('Username has already been taken.')


class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember me')
    submit =SubmitField('Log in')
