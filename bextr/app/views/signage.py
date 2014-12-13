from flask import Blueprint, render_template
from app.content import (
    c_global,
    c_signage,
    c_indoor_signage,
    c_outdoor_signage)


signage = Blueprint('signage', __name__)


@signage.route('/signage/')
def v_signage():
    return render_template('signage.html', c_global=c_global, c_page=c_signage)


@signage.route('/signage/indoor-signage')
def v_indoor_signage():
    return render_template('product.html',
                           c_global=c_global, c_page=c_indoor_signage)


@signage.route('/signage/outdoor-signage')
def v_outdoor_signage():
    return render_template('product.html',
                           c_global=c_global, c_page=c_outdoor_signage)
