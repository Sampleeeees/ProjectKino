import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KinoCMS.settings')

app = Celery('KinoCMS')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_test(self):
    print(f'Request: {self.request!r}')