import json
from os.path import join, abspath


cont_dir = abspath('app/content')


# Global content (header, footer, etc.)

with open(join(cont_dir, 'global.json')) as j_file:
    c_global = json.load(j_file)


# Top level pages

with open(join(cont_dir, 'home.json')) as j_file:
    c_home = json.load(j_file)

with open(join(cont_dir, 'touchscreens.json')) as j_file:
    c_touchscreens = json.load(j_file)

with open(join(cont_dir, 'signage.json')) as j_file:
    c_signage = json.load(j_file)

with open(join(cont_dir, 'about.json')) as j_file:
    c_about = json.load(j_file)

with open(join(cont_dir, 'contact.json')) as j_file:
    c_contact = json.load(j_file)


# Products

with open(join(cont_dir, 'indoor_kiosks.json')) as j_file:
    c_indoor_kiosks = json.load(j_file)

with open(join(cont_dir, 'outdoor_kiosks.json')) as j_file:
    c_outdoor_kiosks = json.load(j_file)

with open(join(cont_dir, 'touch_tables.json')) as j_file:
    c_touch_tables = json.load(j_file)

with open(join(cont_dir, 'touch_windows.json')) as j_file:
    c_touch_windows = json.load(j_file)

with open(join(cont_dir, 'indoor_signage.json')) as j_file:
    c_indoor_signage = json.load(j_file)

with open(join(cont_dir, 'outdoor_signage.json')) as j_file:
    c_outdoor_signage = json.load(j_file)
