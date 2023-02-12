import redis
from django.core.mail import send_mail
from celery import shared_task
from django.conf import settings

@shared_task()
def send_email_task(email_address_list, message):
    # client = redis.Redis(host='127.0.0.1')
    for i in email_address_list:
        send_mail(
            "KinoCMS",
            "About Cinema",
            settings.EMAIL_HOST_USER,
            [i],
            html_message=message,
            fail_silently=False
        )