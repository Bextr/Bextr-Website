from flask import Blueprint, render_template
from ..content import cont_contact


contact = Blueprint('contact', __name__)


@contact.route('/contact')
def r_contact():
    return render_template('contact.html', cont=cont_contact)
