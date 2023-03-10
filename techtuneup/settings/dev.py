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

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/techtuneup.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": "INFO",
        },
    }
}


MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

TIME_ZONE = 'EST'

# use the testing recaptcha key from google
RECAPTCHA_KEY = '6Lfm6aIgAAAAAG61Bl-U4zr0I2XWKwQ_7JS__QOJ'

DOMAIN = 'http://127.0.0.1:8000/'