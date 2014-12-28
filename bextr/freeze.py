from os import environ
environ['FREEZING_SITE'] = '1'
from os.path import exists
from shutil import rmtree
from flask_frozen import Freezer
from app import create_app


app = create_app('config')

freezer = Freezer(app)

build_dir = app.config['FREEZER_DESTINATION']
if exists(build_dir):
    rmtree(build_dir)

freezer.freeze()
# serve the frozen site for testing at http://127.0.0.1:5000
freezer.serve()
