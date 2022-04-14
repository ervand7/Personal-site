import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_site.settings')

app = Celery(__name__)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sending-daily-newsletter': {
        'task': 'subscribe.celery.tasks.send_daily_newsletter',
        'schedule': crontab(minute=0, hour=18),
        'args': (),
    },
}
