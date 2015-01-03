Bextr-Website
=============


##Dependencies

```
pip install --upgrade Flask Flask-SQLAlchemy Flask-WTF Frozen-Flask Flask-Mail Flask-Assets pyyaml markdown cssutils
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


