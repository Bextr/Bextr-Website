from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email, Length


class MessageForm(Form):
    name = StringField('name', validators=[InputRequired(), Length(max=140)])
    email = StringField('email', validators=[InputRequired(), Email(), Length(max=140)])
    text = TextAreaField('text', validators=[InputRequired(), Length(max=500)])


class SubscribeForm(Form):
    email = StringField('email', validators=[InputRequired(), Email(), Length(max=140)])
