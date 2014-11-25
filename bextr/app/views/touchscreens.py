from flask import Blueprint, render_template
from ..content import cont_global, cont_touchscreens


touchscreens = Blueprint('touchscreens', __name__)


@touchscreens.route('/touchscreens')
def r_touchscreens():
    return render_template('touchscreens.html',
                           c_global=cont_global, c_page=cont_touchscreens)
