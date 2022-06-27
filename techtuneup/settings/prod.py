from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.techtuneup.org', 'techtuneup.org']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'service': 'techtuneup',
            'passfile': '.my_pgpass',
        },
    }
}


# default static files settings for PythonAnywhere.
# see https://help.pythonanywhere.com/pages/DjangoStaticFiles for more info
MEDIA_ROOT = '/home/bwalters89/techtuneup/media'
MEDIA_URL = '/media/'
STATIC_ROOT = '/home/bwalters89/techtuneup/static'
STATIC_URL = '/static/'

TIME_ZONE = 'UTC'

# use the production recaptcha key from google
RECAPTCHA_KEY = '6Ldv46MgAAAAAPsZUcAwvihjeiXc0zuKikNWeOBh'