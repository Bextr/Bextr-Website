from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email, Length


class MessageForm(Form):

    name = StringField('Name', validators=[
                       InputRequired(),
                       Length(min=1, max=200)])

    email = StringField('Email', validators=[
                        InputRequired(),
                        Length(min=1, max=200),
                        Email()])

    text = TextAreaField('Message', validators=[
                         InputRequired(),
                         Length(min=1, max=500)])


class SubscribeForm(Form):

    email = StringField('Email', validators=[
                        InputRequired(),
                        Length(min=1, max=200),
                        Email()])
