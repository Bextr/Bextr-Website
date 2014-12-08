import os
from os.path import join, abspath, dirname

_basedir = abspath(dirname(__file__))

DEBUG = True

FROZEN = False

ADMINS = frozenset(['youremail@yourdomain.com'])
SECRET_KEY = 'This string will be replaced with a proper key.'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_basedir, 'storage.sqlite')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2

WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = 'This string will be replaced with a proper key.'
WTF_CSRF_TIME_LIMIT = 3600

JSONIFY_PRETTYPRINT_REGULAR = False
# SESSION_COOKIE_SECURE = True
# PREFERRED_URL_SCHEME = 'https'
JSON_AS_ASCII = False


