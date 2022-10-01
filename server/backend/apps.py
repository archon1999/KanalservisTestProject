from django.apps import AppConfig
from django.utils import timezone


class BackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend'

    def ready(self):
        from . import signals
