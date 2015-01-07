from os import environ, remove
environ['FREEZING_SITE'] = '1'
from os.path import join, isdir, isfile
from shutil import rmtree
from flask_frozen import Freezer
from app import create_app
from app.assets import assets


app = create_app('config')

freezer = Freezer(app)

build_dir = app.config['FREEZER_DESTINATION']
if isdir(build_dir):
    rmtree(build_dir)

freezer.freeze()

# Delete development assets from the build directory.
for k, v in assets._named_bundles.items():
    for asset in v.contents:
        asset_path = join(build_dir, 'static', asset)
        if isfile(asset_path):
            remove(asset_path)

# Serve the frozen site for testing at http://127.0.0.1:5000.
# freezer.serve()
