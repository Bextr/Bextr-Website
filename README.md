Bextr-Website
=============


##Dependencies

```
pip install --upgrade Flask Flask-SQLAlchemy Flask-WTF Frozen-Flask Flask-Mail Flask-Assets pyyaml markdown cssutils html5lib beautifulsoup4
```


##Notes

* Content is declared in yaml files (short tutorial [here](http://learnxinyminutes.com/docs/yaml/)) which are kept in `bextr/app/content`, a file usually equals to a page, exept for header/footer content (`global.yml`) and product lists (`signage_products.yml` and `touchscreen_products.yml`)
* Linked files (images, documents, etc.) are kept in `bextr/app/static`
* When declaring a file path in your yaml files, the path should be relative to the `static` folder (for `bextr/app/static/img/img_1.png` use `img/img_1.png`)
* 


##Changing text
Text is edited by changing the proper value in the respective yaml file.

####Changing the home page title

Edit the value of [page_title](https://github.com/Bextr/Bextr-Website/blob/master/bextr/app/content/home.yml#L1) in `home.yml`.

####Changing the description below the secondary carousel on the home page

Edit the value of [description](https://github.com/Bextr/Bextr-Website/blob/master/bextr/app/content/home.yml#L108) in `home.yml`.

####Changing the copy text in the Call section of the contact page

Edit the value of [call->text](
https://github.com/Bextr/Bextr-Website/blob/master/bextr/app/content/contact.yml#L4) in `home.yml`.


##Editing carousel content

####Adding a new slide

Slides  on the main carousel are declared in a list assigned to the [main_carousel](https://github.com/Bextr/Bextr-Website/blob/master/bextr/app/content/home.yml#L2) key. Add a new item to this list to declare a new slide, the order of the slides is determined by their position in the list.

```yaml
# structure of a slide
    - title: Touchscreens
      text: Accept orders receive payments from unmanned tablet stations
      action:
          text: Learn more
          url: /touchscreens/  # main link
      img:
          file: img/img_2.png  # carousel image
          url: /touchscreens/  # image link
          desc: ""  # alt text
```

####Updating a slide's image

Add the new image file to `bextr/app/static/img` and update the path under the slide's `img->file` key.

```yaml
    - title: Touchscreens
      text: Accept orders receive payments from unmanned tablet stations
      action:
          text: Learn more
          url: /touchscreens/
      img:
          file: img/new_image.png  # carousel image
          url: /touchscreens/
          desc: ""
```


The same principles apply to the rest of the carousels, like the [secondary carousel](https://github.com/Bextr/Bextr-Website/blob/master/bextr/app/content/home.yml#L21), [client carousel](https://github.com/Bextr/Bextr-Website/blob/master/bextr/app/content/home.yml#L111) and [product carousel](https://github.com/Bextr/Bextr-Website/blob/master/bextr/app/content/touchscreens.yml#L2).

####Viewing content in a lightbox (secondary carousel)

Linked content can be opened in lightboxes by specifying the lightbox type.
The `lightbox` key is optional and should only be present when needed.

#####Examples

######Image lightbox

```yaml
    - title: Digital Signage
      text: Lorem ipsum dolor sit amet
      action:
          text: View
          url: /static/img/img_1.png # open this image in a lightbox
          lightbox: image
      img:
          file: img/img_1.png
          url: /static/img/img_1.png # open this image image directly, no lightbox
          desc: ""
```

######Video lightbox

For videos use the following url template and replace `VDEO_ID`.

```
YouTube:
http://www.youtube.com/embed/VDEO_ID?rel=0&wmode=transparent

Vimeo:
http://player.vimeo.com/video/VDEO_ID
```

In this example both the main link and the image will open the same video:
```yaml
    - title: Bextr on the field
      text: Lorem ipsum dolor sit amet consectetur adipiscing elit
      action:
          text: Watch
          url: "http://www.youtube.com/embed/VOJyrQa_WR4?rel=0&wmode=transparent"
          lightbox: video
      img:
          file: img/video_thumb.jpg
          url: "http://www.youtube.com/embed/VOJyrQa_WR4?rel=0&wmode=transparent"
          desc: ""
          lightbox: video
```


##Add a new product

New products can be created by adding them in the appropiate product list,
declaring the product page content in a yaml file and adding a new flask view
to the product category blueprint.

In this example we will add `Product B` to the Signage category.

First we add the product to our [product menu](https://github.com/Bextr/Bextr-Website/blob/master/bextr/app/content/signage_products.yml):

```yaml
- title: Indoor Signage
  file: svg/indoor_kiosk.svg
  url: /signage/indoor-signage
  desc: ""
- title: Outdoor Signage
  file: svg/outdoor_kiosk.svg
  url: /signage/outdoor-signage
  desc: ""
- title: Product B
  file: svg/product_b.svg # menu image
  url: /signage/product-b # the same as the flask view's route
  desc: ""
```


Now we must declare the product page content by creating a new yaml file named
`product_b.yml` (the name can be different but we will reference this when 
loading the content).
Use [indoor_signage.yml](https://github.com/Bextr/Bextr-Website/blob/master/bextr/app/content/indoor_signage.yml)
as a template for the new file's content.

```yaml
page_title: Bextr - Product C
products: !include signage_products.yml
main_carousel:
...
```


The next step is to load the content and store it in a variable, this is done
in [`__init__.py`](https://github.com/Bextr/Bextr-Website/blob/master/bextr/app/content/__init__.py#L80) of the `content` folder.

Load the content like this:
```python
c_product_b = load('product_b.yml')
```


A flask view must be created that serves the product page, we do this in the
[signage blueprint](https://github.com/Bextr/Bextr-Website/blob/master/bextr/app/views/signage.py).

Here is the final state of the blueprint:
```python
from flask import Blueprint, render_template
from app.content import (
    c_global,
    c_signage,
    c_indoor_signage,
    c_outdoor_signage
    c_product_b)  # import our product content


signage = Blueprint('signage', __name__)


@signage.route('/signage/')
def v_signage():
    return render_template('signage.html', c_global=c_global, c_page=c_signage)


@signage.route('/signage/indoor-signage')
def v_indoor_signage():
    return render_template('product.html',
                           c_global=c_global, c_page=c_indoor_signage)


@signage.route('/signage/outdoor-signage')
def v_outdoor_signage():
    return render_template('product.html',
                           c_global=c_global, c_page=c_outdoor_signage)

# Declare a new view and route for Product B.
@signage.route('/signage/product-b') # the same as the url in the product menu
def v_product_b():
    return render_template('product.html',
                           c_global=c_global, c_page=c_product_b)  # feed the content to the jinja2 template
```


That's it, the product page should be viewabe (after restarting/refreezing the
app) by visiting `domain.com/signage/product-b`.


##Add a top level page

This is similar to adding a new product, but we must also create a new jinja2
template and a blueprint with views (this is not mandatory, but blueprints
are good for organizing views and making them easily pluggable).

Let's add a new product category called `Category B`.

First we should add a link to the main menu, this is done in
[global.yml](https://github.com/Bextr/Bextr-Website/blob/master/bextr/app/content/global.yml).

```yaml
site_desc: ""
site_kw: touchscreens, kiosks, digital signage
header:
    logo:
        file: svg/bextr_logo.svg
        url: /
        desc: bextr logo
    menu:
        - text: TOUCHSCREENS
          url: /touchscreens/
        - text: SIGNAGE
          url: /signage/
        - text: Category B  # page name
          url: /category-b/  # intended url (same as for the blueprint's view)
        - text: ABOUT
          url: /about
        - text: CALL US
          url: /contact
...
```


The page content is declared in a new file called `category_b.yml`.
Use a category page content file
([touchscreens.yml](https://github.com/Bextr/Bextr-Website/blob/master/bextr/app/content/touchscreens.yml))
as a template.

```yml
page_title: Bextr - Category B
products: !include category_b_products.yml
main_carousel:
...
```


Create a product list, `category_b_products.yml`.
Use [signage_products.yml](https://github.com/Bextr/Bextr-Website/blob/master/bextr/app/content/signage_products.yml) as a template.


Load the page content in 
[`__init__.py`](https://github.com/Bextr/Bextr-Website/blob/master/bextr/app/content/__init__.py#L71).

```python
c_category_b = load('category_b.yml')
```


Create a new jinja2 template in `bextr/app/templates/`, let's call it
`category_b.html`.

```
{% extends "layout.html" %}
{% from 'template_macros.html' import cta, main_crs, sec_crs, product_crs %}

{%- block content %}
{{- product_crs(c_page.products) }}
{{- main_crs(c_page.main_carousel) }}
{{- cta(c_page.cta.top) }}
{{- sec_crs(c_page.sec_carousel) }}
{{- cta(c_page.cta.bottom) }}
{%- endblock content %}
```


A blueprint with the needed views must be created, create a new file in
`bextr/app/views/` named `category_b.py`.

```python
from flask import Blueprint, render_template
from app.content import (
    c_global,
    c_category_b)


category_b = Blueprint('category_b', __name__)


@category_b.route('/category-b/')
def v_category_b():
    return render_template('category_b.html', c_global=c_global, c_page=c_category_b)

# Product views are declared below

```

Import the blueprint in views
[`__init__.py`](https://github.com/Bextr/Bextr-Website/blob/master/bextr/app/views/__init__.py).

```python
from .category_b import category_b
```

The final step is to register the blueprint in app
[`__init__.py`](https://github.com/Bextr/Bextr-Website/blob/master/bextr/app/__init__.py#L20).

```python
...
    if not app.config['FROZEN_SITE']:
        from app.assets import assets
        assets.init_app(app)
        from app.views import home, touchscreens, signage, about, contact, category_b
        app.register_blueprint(home)
        app.register_blueprint(touchscreens)
        app.register_blueprint(signage)
        app.register_blueprint(about)
        app.register_blueprint(contact)
        app.register_blueprint(category_b)
...
```


##Text styling
Page styling is largely done in `bextr/app/static/css/style.css`.
The stylesheet is divided in sections for easier navigation.

All textual content can be styled with markdown where needed.

This is done by replacing a simple string in our yaml files with a dictionary
(`{'markup': True, 'data': 'this is our **text**'}`).

```yaml
# text without markdown
text: this is our text

# the same text with markdown
text:
    markup: true
    data: this is our **text**
```

When the content is loaded this dictionary is processed and replaced with a
rendered html string.


##Freezing

Simply run `python freeze.py`. A `build` folder is created which contains the
entire static site. This content should be served with nginx.

The site api is needed for the contact page forms, this should be served
by coupling the flask app with gunicorn and nginx.
`FROZEN_SITE` must be set to `True` in
[config.py](https://github.com/Bextr/Bextr-Website/blob/master/bextr/config.py),
also set `DEBUG = False` for security reasons.
If `FROZEN_SITE` is `True`, only the api blueprint is registered for the app.
This way we can use the same app for a fully dynamic site, or serve just an api
and freeze the rest of the site.

