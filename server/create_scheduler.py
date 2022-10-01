import os

import class_settings
from class_settings import env
from django.core.wsgi import get_wsgi_application

env.read_env()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
os.environ.setdefault('DJANGO_SETTINGS_CLASS', 'CoreSettings')
class_settings.setup()
application = get_wsgi_application()

if __name__ == '__main__':
    from django_q.tasks import Schedule
    from django.utils import timezone

    next_run = timezone.now().replace(hour=0, minute=0, second=0)
    name = 'update-data'
    if not Schedule.objects.filter(name=name).exists():
        Schedule.objects.create(
            name=name,
            func='backend.tasks.update_data',
            schedule_type=Schedule.MINUTES,
            minutes=1,
        )

    name = 'update-ruble-exchange-rate'
    if not Schedule.objects.filter(name=name).exists():
        Schedule.objects.create(
            name=name,
            func='backend.tasks.update_ruble_exchange_rate',
            schedule_type=Schedule.DAILY,
            next_run=next_run,
        )
