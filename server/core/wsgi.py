import os

import class_settings
from class_settings import env
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

env.read_env()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
os.environ.setdefault('DJANGO_SETTINGS_CLASS', 'CoreSettings')
class_settings.setup()

application = get_wsgi_application()
application = WhiteNoise(application)
application.add_files('static', prefix='static/')
