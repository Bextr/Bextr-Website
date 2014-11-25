from flask import Blueprint, render_template
from ..content import cont_global, cont_about


about = Blueprint('about', __name__)


@about.route('/about')
def r_about():
    return render_template('about.html',
                           c_global=cont_global, c_page=cont_about)
