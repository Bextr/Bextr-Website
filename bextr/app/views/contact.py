from flask import Blueprint, render_template
from ..content import c_global, c_contact


contact = Blueprint('contact', __name__)


@contact.route('/contact')
def v_contact():
    return render_template('contact.html', c_global=c_global, c_page=c_contact)
