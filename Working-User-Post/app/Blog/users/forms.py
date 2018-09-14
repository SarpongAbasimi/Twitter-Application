from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class Postform(FlaskForm):
    content=TextAreaField('content',validators=[DataRequired()])
    submit=SubmitField('Tweet')
