from flask import Blueprint, render_template
from ..content import cont_global, cont_signage


signage = Blueprint('signage', __name__)


@signage.route('/signage')
def r_signage():
    return render_template('signage.html',
                           c_global=cont_global, c_page=cont_signage)
