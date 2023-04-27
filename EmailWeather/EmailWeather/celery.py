from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings
# from django_celery_beat.models import PeriodicTask, CrontabSchedule
# from emailapp.tasks import send_mail_task
from datetime import timedelta, datetime
# import datetime


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EmailWeather.settings')

app = Celery('EmailWeather')
app.conf.enable_utc=False

app.config_from_object(settings, namespace='CELERY')

app.conf.timezone='Africa/Lagos'

# schedule = CrontabSchedule.objects.create(
#     minute='*/1',
# )

# task = PeriodicTask.objects.create(
#     name='my_task',
#     task='emailapp.tasks.send_mail_task',
#     crontab=schedule,
#     start_time=datetime.now(),
#     expires=datetime.now() + timedelta(days=1),
# )

# task.save()

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

now = datetime.now()
target_time = datetime.combine(now.date(), datetime.strptime('06:00', '%H:%M').time()) #to run by 6:00 a.m. everyday
delta = (target_time - now) % timedelta(days=1)

app.conf.beat_schedule = {
    'Send_mail_to_Client': {
    'task': 'emailapp.tasks.send_mail_task',
    'schedule': delta, 
    # 'args': (16, 16)
    }
    }

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')