from flask.ext.assets import Environment, Bundle


assets = Environment()

js = Bundle('js/jquery-ui.js', 'js/script.js',
            filters='rjsmin', output='js/packed.min.js')
assets.register('js_all', js)

css = Bundle('css/style.css',
             filters='cssutils', output='css/packed.min.css')
assets.register('css_all', css)
