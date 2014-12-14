from flask import escape, current_app
from flask_mail import Mail, Message

mail = Mail()


def fwd_site_message(name, email, message):
    msg = Message('Message from ' + escape(name),
                  recipients=current_app.config['MAIL_FORWARD_TO'],
                  reply_to=escape(email),
                  body=escape(message))
    mail.send(msg)
