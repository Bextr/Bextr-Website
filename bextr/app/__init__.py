from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

if not app.config['FREEZING_SITE']:
    from app.views import api
    app.register_blueprint(api)

if not app.config['FROZEN_SITE']:
    from app.views import home, touchscreens, signage, about, contact
    app.register_blueprint(home)
    app.register_blueprint(touchscreens)
    app.register_blueprint(signage)
    app.register_blueprint(about)
    app.register_blueprint(contact)
