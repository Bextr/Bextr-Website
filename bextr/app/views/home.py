from flask import Blueprint, render_template
from app.content import c_global, c_home


home = Blueprint('home', __name__)


@home.route('/')
def v_home():
    return render_template('home.html', c_global=c_global, c_page=c_home)
