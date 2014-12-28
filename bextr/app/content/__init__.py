import json
import markdown
from yaml import safe_load
from flask import Markup
from os.path import join, abspath, dirname


cont_dir = abspath(dirname(__file__))


def process_markup_hook(obj):
    if 'markup' in obj and obj['markup'] is True:
        mrk = markdown.markdown(obj['data'],
                                output_format='html5',
                                extensions=['markdown.extensions.extra'])
        return Markup(mrk)
    return obj


def process_markup(obj):
    return json.loads(json.dumps(obj), object_hook=process_markup_hook)


# Global content (header, footer, etc.)

with open(join(cont_dir, 'global.yml'), encoding='utf-8') as file:
    c_global = process_markup(safe_load(file))


# Top level pages

with open(join(cont_dir, 'home.yml'), encoding='utf-8') as file:
    c_home = process_markup(safe_load(file))

with open(join(cont_dir, 'touchscreens.yml'), encoding='utf-8') as file:
    c_touchscreens = process_markup(safe_load(file))

with open(join(cont_dir, 'signage.yml'), encoding='utf-8') as file:
    c_signage = process_markup(safe_load(file))

with open(join(cont_dir, 'about.yml'), encoding='utf-8') as file:
    c_about = process_markup(safe_load(file))

with open(join(cont_dir, 'contact.yml'), encoding='utf-8') as file:
    c_contact = process_markup(safe_load(file))


# Products

with open(join(cont_dir, 'touch_tables.yml'), encoding='utf-8') as file:
    c_touch_tables = process_markup(safe_load(file))

with open(join(cont_dir, 'touch_windows.yml'), encoding='utf-8') as file:
    c_touch_windows = process_markup(safe_load(file))

with open(join(cont_dir, 'indoor_signage.yml'), encoding='utf-8') as file:
    c_indoor_signage = process_markup(safe_load(file))

with open(join(cont_dir, 'outdoor_signage.yml'), encoding='utf-8') as file:
    c_outdoor_signage = process_markup(safe_load(file))

with open(join(cont_dir, 'indoor_kiosks.yml'), encoding='utf-8') as file:
    c_indoor_kiosks = process_markup(safe_load(file))

with open(join(cont_dir, 'outdoor_kiosks.yml'), encoding='utf-8') as file:
    c_outdoor_kiosks = process_markup(safe_load(file))
