from flask import Blueprint, render_template
from ..content import cont_home


home = Blueprint('home', __name__)


@home.route('/')
def r_home():
    return render_template('homepage.html', cont=cont_home)
