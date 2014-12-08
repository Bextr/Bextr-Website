from flask import Blueprint, abort
from ..forms import MessageForm, SubscribeForm


api = Blueprint('api', __name__)


@api.route('/api/message', methods=['POST'])
def v_message():
    msg_form = MessageForm(prefix='message')

    if msg_form.validate_on_submit():
        print(msg_form.name.data)
        print(msg_form.email.data)
        print(msg_form.text.data)
        return '', 204
    abort(400)
