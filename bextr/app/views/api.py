from flask import Blueprint, abort
from flask_wtf import Form
from ..forms import MessageForm, SubscribeForm


api = Blueprint('api', __name__)


@api.route('/api/csrf-token', methods=['GET'])
def v_csrf():
    return Form().generate_csrf_token()


@api.route('/api/message', methods=['POST'])
def v_message():
    form = MessageForm(prefix='message')

    if form.validate_on_submit():
        print(form.name.data)
        print(form.email.data)
        print(form.text.data)
        return '', 204
    abort(400)


@api.route('/api/subscribe', methods=['POST'])
def v_subscribe():
    form = SubscribeForm(prefix='subscribe')

    if form.validate_on_submit():
        print(form.email.data)
        return '', 204
    abort(400)
