from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EmailWeather.settings')

app = Celery('EmailWeather')
app.conf.enable_utc=False

app.config_from_object(settings, namespace='CELERY')

app.conf.timezone='Africa/Lagos'

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'Send_mail_to_Client': {
    'task': 'emailapp.tasks.send_mail_task',
    'schedule': crontab(hour='9', minute='30'), 
    # 'args': (16, 16)
    }
    }

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')