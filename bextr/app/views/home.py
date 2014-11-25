from flask import Blueprint, render_template
from ..content import cont_global, cont_home


home = Blueprint('home', __name__)


@home.route('/')
def r_home():
    return render_template('home.html',
                           c_global=cont_global, c_page=cont_home)
