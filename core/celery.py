import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
#это в часах и минутах
app.conf.beat_schedule = {
    'send_email': {
        'task': 'apps.users.tasks.send_email',
        'schedule': crontab(minute=43, hour=16),
        'kwargs': {},
    },
#это в секундах
    # 'send_email_2': {
    #     'task': 'apps.users.tasks.send_email',
    #     'schedule': 10.0,
    #     'kwargs': {},
    # }

}