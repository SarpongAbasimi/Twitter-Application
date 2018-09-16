from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length

class PostForm(FlaskForm):
    content=TextAreaField('content',validators=[DataRequired()])
    submit=SubmitField('Tweet')

class EditForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    about_me=TextAreaField('About me',validators=[DataRequired(),Length(min=1 ,max=10)])
    location=StringField('Location',validators=[DataRequired()])
    submit=SubmitField('Edit profile')
