DEFAULT_APPS = [
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'backend',
    'ws',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'django_q',
    'django_filters',
    'jet',
    'rest_framework',
    'channels',
    'solo',
]

INSTALLED_APPS = THIRD_PARTY_APPS + DEFAULT_APPS + LOCAL_APPS
