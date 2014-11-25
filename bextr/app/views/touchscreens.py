from flask import Blueprint, render_template
from ..content import cont_touchscreens


touchscreens = Blueprint('touchscreens', __name__)


@touchscreens.route('/touchscreens')
def r_touchscreens():
    return render_template('touchscreens.html', cont=cont_touchscreens)
