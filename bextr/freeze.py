from os import environ, remove, walk
environ['FREEZING_SITE'] = '1'
from os.path import join, isdir, isfile
from shutil import rmtree
from flask_frozen import Freezer
from app import create_app
from app.assets import assets
# from app.utils.minify import html_minify

app = create_app('config')

freezer = Freezer(app)

build_dir = app.config['FREEZER_DESTINATION']
if isdir(build_dir):
    rmtree(build_dir)

freezer.freeze()

# Delete development assets in the build directory.
for k, v in assets._named_bundles.items():
    for asset in v.contents:
        asset_path = join(build_dir, 'static', asset)
        if isfile(asset_path):
            remove(asset_path)

# Delete webassets cache folder.
assets_cache = join(build_dir, 'static', '.webassets-cache')
if isdir(assets_cache):
    rmtree(assets_cache)

# Minify html files. Not used until the footer is fixed. bs4 must output html5.
# for root, subdirs, files in walk(build_dir):
#     for fl in files:
#         if fl.endswith('.html') or '.' not in fl:
#             with open(join(root, fl), mode='r+', encoding='utf-8') as file:
#                 minified = html_minify(file, ignore_comments=False)
#                 file.truncate(0)
#                 file.seek(0)
#                 file.write(minified)


# Serve the frozen site for testing at http://127.0.0.1:5000.
# freezer.serve()
