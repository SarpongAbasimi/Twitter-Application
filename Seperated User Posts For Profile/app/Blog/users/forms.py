from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length
from flask_login import current_user
from Blog.models import User

class PostForm(FlaskForm):
    content=TextAreaField('content',validators=[DataRequired()])
    submit=SubmitField('Tweet')

class EditForm(FlaskForm):
    username=StringField('Username',validators=[Length(min=0, max=15)])
    about_me=TextAreaField('About me',validators=[Length(min=0 ,max=15)])
    location=StringField('Location',validators=[Length(min=0, max=15)])
    submit=SubmitField('Edit profile')
    save_me=SubmitField('Save changes')

    def validate_username(self,username):
        if username.data != current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise validationError('Username is already taken')
