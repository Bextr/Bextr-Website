from flask import Blueprint, render_template
from ..content import c_global, c_about


about = Blueprint('about', __name__)


@about.route('/about')
def v_about():
    return render_template('about.html', c_global=c_global, c_page=c_about)
