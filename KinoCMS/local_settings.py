import os
import environ
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env()
environ.Env.read_env()



SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['143.198.148.29']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIAFILES_DIRS = [
    os.path.join(BASE_DIR, 'media')
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'rubetsdima2004@gmail.com'
EMAIL_HOST_PASSWORD = 'gheslkacgwwucmwa'
EMAIL_PORT = 587



CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"