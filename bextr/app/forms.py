from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email, Length


class MessageForm(Form):

    name = StringField('name', validators=[
                       InputRequired(),
                       Length(min=1, max=200)])

    email = StringField('email', validators=[
                        InputRequired(),
                        Email(),
                        Length(min=1, max=200)])

    text = TextAreaField('text', validators=[
                         InputRequired(),
                         Length(min=1, max=500)])


class SubscribeForm(Form):

    email = StringField('email', validators=[
                        InputRequired(),
                        Email(),
                        Length(max=200)])
