from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.techtuneup.org', 'techtuneup.org']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# default static files settings for PythonAnywhere.
# see https://help.pythonanywhere.com/pages/DjangoStaticFiles for more info
MEDIA_ROOT = '/home/ubuntu/TechTuneUp/media'
MEDIA_URL = '/media/'
STATIC_ROOT = '/home/ubuntu/TechTuneUp/static'
STATIC_URL = '/static/'

TIME_ZONE = 'UTC'

# use the production recaptcha key from google
RECAPTCHA_KEY = '6LcoP6EgAAAAAG0zexEA83UDaxn-KzvoFa9mDZFJ'

DOMAIN = 'http://www.techtuneup.org/'