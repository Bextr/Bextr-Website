from flask import Blueprint, abort, escape, current_app
from flask_wtf import Form
from flask_mail import Mail, Message
from time import time
from app.forms import MessageForm, SubscribeForm
from app.models import db, Subscriber


mail = Mail()
_s = db.session
api = Blueprint('api', __name__)


def epoch():
    return int(time())


@api.route('/api/csrf-token', methods=['GET'])
def v_csrf():
    return Form().generate_csrf_token()


@api.route('/api/message', methods=['POST'])
def v_message():
    form = MessageForm(prefix='message')

    if form.validate_on_submit():
        msg = Message('Message from ' + escape(form.name.data),
                      recipients=current_app.config['MAIL_FORWARD_TO'],
                      reply_to=escape(form.email.data),
                      body=escape(form.text.data))
        mail.send(msg)
        return '', 204
    abort(400)


@api.route('/api/subscribe', methods=['POST'])
def v_subscribe():
    form = SubscribeForm(prefix='subscribe')

    if form.validate_on_submit():
        email = escape(form.email.data)
        if not _s.query(Subscriber).filter(Subscriber.email == email).first():
            subs = Subscriber(epoch=epoch(), email=email)
            _s.add(subs)
            _s.commit()
            return '', 204
        abort(409)
    abort(400)
