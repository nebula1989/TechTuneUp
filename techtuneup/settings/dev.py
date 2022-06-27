from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
from .base import BASE_DIR

SECRET_KEY = 'django-insecure-7w_)c3-&$n86xh2lqi)jgi+2uim_(u8i)om57m=lf&v9na60n!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

TIME_ZONE = 'EST'

SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']