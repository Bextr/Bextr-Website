import os
from os.path import join, abspath, dirname

_basedir = abspath(dirname(__file__))

DEBUG = True
THREADS_PER_PAGE = 2
JSONIFY_PRETTYPRINT_REGULAR = False
# SESSION_COOKIE_SECURE = True
# PREFERRED_URL_SCHEME = 'https'
JSON_AS_ASCII = False
SECRET_KEY = 'This string will be replaced with a proper key.'

WTF_CSRF_SECRET_KEY = 'This string will be replaced with a proper key.'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_basedir, 'storage.sqlite')

FREEZER_DESTINATION = join(_basedir, 'build')
FREEZER_DEFAULT_MIMETYPE = 'text/html'

MAIL_SERVER = 'smtp.mailgun.org'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_DEBUG = False
MAIL_USERNAME = 'postmaster@sandbox68069f340da74480a0d43c44f2c89c23.mailgun.org'
MAIL_PASSWORD = '7be88edd2da4200289f6b6dd3dd8ae64'
MAIL_DEFAULT_SENDER = MAIL_USERNAME
MAIL_MAX_EMAILS = None
MAIL_SUPPRESS_SEND = False
MAIL_ASCII_ATTACHMENTS = False

MAIL_FORWARD_TO = ['zauvareo@zoho.com']

FROZEN_SITE = False
FREEZING_SITE = int(os.getenv('FREEZING_SITE', '0'))
