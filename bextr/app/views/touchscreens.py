from flask import Blueprint, render_template
from app.content import (
    c_global,
    c_touchscreens,
    c_indoor_kiosks,
    c_outdoor_kiosks,
    c_touch_tables,
    c_touch_windows
    )


touchscreens = Blueprint('touchscreens', __name__)


@touchscreens.route('/touchscreens/')
def v_touchscreens():
    return render_template('touchscreens.html',
                           c_global=c_global, c_page=c_touchscreens)


@touchscreens.route('/touchscreens/indoor-kiosks')
def v_indoor_kiosks():
    return render_template('product.html',
                           c_global=c_global, c_page=c_indoor_kiosks)


@touchscreens.route('/touchscreens/outdoor-kiosks')
def v_outdoor_kiosks():
    return render_template('product.html',
                           c_global=c_global, c_page=c_outdoor_kiosks)


@touchscreens.route('/touchscreens/touch-tables')
def v_touch_tables():
    return render_template('product.html',
                           c_global=c_global, c_page=c_touch_tables)


@touchscreens.route('/touchscreens/touch-windows')
def v_touch_windows():
    return render_template('product.html',
                           c_global=c_global, c_page=c_touch_windows)
