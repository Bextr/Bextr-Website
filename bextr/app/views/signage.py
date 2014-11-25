from flask import Blueprint, render_template
from ..content import cont_signage


signage = Blueprint('signage', __name__)


@signage.route('/signage')
def r_signage():
    return render_template('signage.html', cont=cont_signage)
