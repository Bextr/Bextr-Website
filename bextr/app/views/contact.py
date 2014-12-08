from flask import Blueprint, render_template
from ..content import c_global, c_contact
from ..forms import MessageForm, SubscribeForm


contact = Blueprint('contact', __name__)


@contact.route('/contact', methods=['GET', 'POST'])
def v_contact():
    msg_form = MessageForm(prefix='message')
    subs_form = SubscribeForm(prefix='subscribe')
    return render_template('contact.html',
                           c_global=c_global,
                           c_page=c_contact,
                           msg_form=msg_form,
                           subs_form=subs_form)
