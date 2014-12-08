from flask import Blueprint, abort
from flask_wtf import Form
from time import time
from ..forms import MessageForm, SubscribeForm
from app.models import Subscriber
from app import db


def epoch():
    return int(time())


api = Blueprint('api', __name__)

_s = db.session

@api.route('/api/csrf-token', methods=['GET'])
def v_csrf():
    return Form().generate_csrf_token()


@api.route('/api/message', methods=['POST'])
def v_message():
    form = MessageForm(prefix='message')

    if form.validate_on_submit():
        print(form.name.data, form.email.data, form.text.data)
        return '', 204
    abort(400)


@api.route('/api/subscribe', methods=['POST'])
def v_subscribe():
    form = SubscribeForm(prefix='subscribe')

    if form.validate_on_submit():
        email = form.email.data
        if not _s.query(Subscriber).filter(Subscriber.email == email).first():
            subs = Subscriber(epoch=epoch(), email=email)
            _s.add(subs)
            _s.commit()
            return '', 204
        abort(409)
    abort(400)
