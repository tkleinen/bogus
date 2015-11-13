"""
Django settings for bogus project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
os.sys.path.append('/home/theo/acaciadata.com/acacia')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'syjhq*)j_47@870=$k6zx8ej=^5ezn)b*8k@fve_cb!%+qe3h='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['.acaciadata.com', 'localhost']

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'polymorphic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'south',
    'registration',
    'acacia',
    'acacia.data',
    'acacia.data.knmi',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bogus.urls'

WSGI_APPLICATION = 'bogus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'NAME': 'bogus',                      # Or path to database file if using sqlite3.
        'USER': 'acacia',                      # Not used with sqlite3.
        'PASSWORD': 'Beaumont1',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'nl-nl'

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGS_URL = '/logs/'
LOGS_ROOT = os.path.join(BASE_DIR, 'logs')

UPLOAD_DATAFILES = 'datafiles' 
UPLOAD_THUMBNAILS = 'thumbnails' 
UPLOAD_IMAGES = 'images' 

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Grapelli admin
GRAPPELLI_ADMIN_TITLE='Beheer van Bogus meetgegevens'

# Celery stuff
#BROKER_URL = 'django://'
CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
INSTALLED_APPS += ('kombu.transport.django','djcelery',)                  

#CELERY_ALWAYS_EAGER = DEBUG

# registration stuff
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = '/data/'

EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='grondwatertoolbox@gmail.com'
EMAIL_HOST_PASSWORD='pw4toolbox'
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = 'noreply@acaciawater.com'

LOGGING_ROOT = os.path.join(BASE_DIR, 'logs')

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOGGING_ROOT, 'acacia.log'),
            'when': 'D',
            'interval': 1, # every day a new file
            'backupCount': 0,
            'formatter': 'default'
        },
        'update': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOGGING_ROOT, 'updater.log'),
            'when': 'D',
            'interval': 1, # every day a new file
            'backupCount': 0,
            'formatter': 'update'
        },
        'django': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOGGING_ROOT, 'django.log'),
            'when': 'D',
            'interval': 1, # every day a new file
            'backupCount': 0,
        },
        'email': {
            'level': 'DEBUG',
            'class': 'acacia.data.loggers.BufferingEmailHandler',
            'fromaddr': 'webmaster@acaciadata.com',
            'subject': 'spaarwater.acaciadata.com update',
            'capacity': 10000,
            'interval': 30,
            'formatter': 'update',
        },
    },
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(name)s: %(message)s'
        },
        'update' : {
            'format': '%(levelname)s %(asctime)s %(datasource)s: %(message)s'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['django'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'acacia.data': {
            'handlers': ['file',],
            'level': 'DEBUG',
            'propagate': True,
        },
        'update' : {
            'handlers': ['update', ],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
