from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')

if not app.config['FROZEN']:
    from flask_bootstrap import Bootstrap
    from .views import home, touchscreens, signage, about, contact
    Bootstrap(app)
    app.register_blueprint(home)
    app.register_blueprint(touchscreens)
    app.register_blueprint(signage)
    app.register_blueprint(about)
    app.register_blueprint(contact)
