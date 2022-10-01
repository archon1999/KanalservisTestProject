from pathlib import Path

import dotenv
from class_settings import Settings, env

from .auth_password_validators import AUTH_PASSWORD_VALIDATORS
from .caches import CACHES
from .channel_layers import CHANNEL_LAYERS
from .cors import (CORS_ALLOW_CREDENTIALS, CORS_ALLOW_HEADERS,
                   CORS_ALLOWED_ORIGINS)
from .databases import DATABASES
from .installed_apps import INSTALLED_APPS
from .logging import LOGGING
from .middleware import MIDDLEWARE
from .q_cluster import Q_CLUSTER
from .rest_framework import REST_FRAMEWORK
from .templates import TEMPLATES

dotenv.load_dotenv(Path(__file__).parent.parent.parent / '.env')

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class CoreSettings(Settings):
    ALLOWED_HOSTS = ['*']
    SECRET_KEY = env()
    DEBUG = env.bool(default=True)
    INSTALLED_APPS = INSTALLED_APPS
    MIDDLEWARE = MIDDLEWARE
    ROOT_URLCONF = 'core.urls'
    WSGI_APPLICATION = 'core.wsgi.application'
    SITE_ID = 1
    ASGI_APPLICATION = "core.asgi.application"
    DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
    TEMPLATES = TEMPLATES
    DATABASES = DATABASES

    AUTH_PASSWORD_VALIDATORS = AUTH_PASSWORD_VALIDATORS
    AUTH_USER_MODEL = 'backend.User'

    LOGGING = LOGGING

    DECIMAL_SEPARATOR = '.'

    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    LANGUAGE_CODE = 'ru-RU'
    TIME_ZONE = 'Europe/Moscow'

    STATIC_DIR = BASE_DIR / 'static'
    STATIC_URL = '/static/'
    STATIC_ROOT = 'static'
    STATICFILES_STORAGE = 'whitenoise.storage.' + \
        'CompressedManifestStaticFilesStorage'

    JET_SIDE_MENU_COMPACT = True

    REST_FRAMEWORK = REST_FRAMEWORK
    CACHES = CACHES
    CHANNEL_LAYERS = CHANNEL_LAYERS
    Q_CLUSTER = Q_CLUSTER

    CORS_ALLOW_CREDENTIALS = CORS_ALLOW_CREDENTIALS
    CORS_ALLOW_HEADERS = CORS_ALLOW_HEADERS
    # CORS_ALLOWED_ORIGINS = CORS_ALLOWED_ORIGINS
    CORS_ALLOW_ALL_ORIGINS = True
