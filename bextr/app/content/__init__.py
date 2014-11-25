import json

with open('app/content/global.json') as json_file:
    cont_global = json.load(json_file)

with open('app/content/home.json') as json_file:
    cont_home = json.load(json_file)

with open('app/content/touchscreens.json') as json_file:
    cont_touchscreens = json.load(json_file)

with open('app/content/signage.json') as json_file:
    cont_signage = json.load(json_file)

with open('app/content/about.json') as json_file:
    cont_about = json.load(json_file)

with open('app/content/contact.json') as json_file:
    cont_contact = json.load(json_file)
