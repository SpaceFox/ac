"""
Django settings for AnneColin project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import locale
import os
import platform

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Python is platform-independent...or is it?
if platform.system() == "Windows":
    locale.setlocale(locale.LC_TIME, 'fra')
else:
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

USE_L10N = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&fd0(o@4zqfke&msfu=grs-5*#l0n5^1s8yw)ilhhv%gs8m23q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'easy_thumbnails',
    'crispy_forms',
    
    'gallery',
)
if (DEBUG):
    INSTALLED_APPS += (   
#       'debug_toolbar',
    )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
if DEBUG:
    MIDDLEWARE_CLASSES += (   
#        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    THUMBNAIL_DEBUG = True

ROOT_URLCONF = 'AnneColin.urls'

WSGI_APPLICATION = 'AnneColin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME'  : 'annecolin',
#        'USER'  : 'annecolin',
#        'PASSWORD'  : 'passw0rd',
#        'HOST'  : 'localhost',
#    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ROOT = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

THUMBNAIL_ALIASES = {
    '': {
        'home': {'size': (165, 165), 'crop': 'smart'},
        'gallery': {'size': (165, 165)},
        'aside': {'size': (90, 90)},
        'picture': {'size': (900, 600)},
    },
}

MAIL_CONTACT = 'ujueseo.yeou@gmail.com'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                # Default context processors
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap'


# Load the production settings, overwrite the existing ones if needed
try:
    from settings_prod import *
except ImportError:
    pass
