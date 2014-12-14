from flask import Flask
from app.models import db
from app.views.api import mail


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)

    if not app.config['FREEZING_SITE']:
        db.init_app(app)
        with app.app_context():
            db.create_all()
        mail.init_app(app)
        from app.views import api
        app.register_blueprint(api)

    if not app.config['FROZEN_SITE']:
        from app.views import home, touchscreens, signage, about, contact
        app.register_blueprint(home)
        app.register_blueprint(touchscreens)
        app.register_blueprint(signage)
        app.register_blueprint(about)
        app.register_blueprint(contact)

    return app
