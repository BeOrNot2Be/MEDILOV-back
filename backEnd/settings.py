"""
Django settings for backEnd project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'medilov',
    'django_feedparser',
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django_user_agents',
]

USER_AGENTS_CACHE = 'default'


ACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

JET_DEFAULT_THEME = 'default'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'backEnd.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backEnd.wsgi.application'

#email 
EMAIL_HOST = os.environ['SMTP_SERVER']
EMAIL_HOST_USER = os.environ['SMTP_USER']
EMAIL_HOST_PASSWORD = os.environ['SMTP_PASSWORD']
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'

if 'DJANGO_DEBUG_FALSE' in os.environ:  
    DEBUG = True
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']  
    ALLOWED_HOSTS = [os.environ["SITENAME"]]
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': os.environ['DBNAME'],
            'HOST': os.environ['DBHOST'],
            'USER': os.environ['DBUSER'],
            'PASSWORD': os.environ['DBUSERPASSWORD']
        }
    }
    WEBSITEHOLDEREMAIL = os.environ['WHEMAIL']
    EMAIL_PORT = os.environ['SMTP_PORT']
    
else:
    DEBUG = False  
    SECRET_KEY = 'ctwj8_&w$vkw2ce&w+$c%8z$m6hpe4f8f8y^#h&_rt_o7na23u'
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', '*']
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'medilov',
        }
    }
    WEBSITEHOLDEREMAIL = "admin@avilonproduction.com"
    EMAIL_PORT = 465

if 'test' in sys.argv:
    DATABASES['default'] = {
            'ENGINE': 'djongo',
            'NAME': 'medilov',
    }
    WEBDRIVER_PATH = os.environ.get('REMOTEBROWESRDRIVER', False)


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    }
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
]


COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False if 'test' in sys.argv else True
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'
COMPRESS_OFFLINE_CONTEXT = {'base_template': "index.html"}
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.rCSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter'
]

TEMPLATES_URL = '/templates/'

django_heroku.settings(locals())

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }   
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'ERROR',
        },
    },
}