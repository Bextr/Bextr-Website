import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

FROZEN = False

ADMINS = frozenset(['youremail@yourdomain.com'])
SECRET_KEY = 'This string will be replaced with a proper key in production.'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2

WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = 'This string will be replaced with a proper key in production.'

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''
RECAPTCHA_OPTIONS = {'theme': 'white'}

JSONIFY_PRETTYPRINT_REGULAR = False
# SESSION_COOKIE_SECURE = True
# PREFERRED_URL_SCHEME = 'https'
JSON_AS_ASCII = False


