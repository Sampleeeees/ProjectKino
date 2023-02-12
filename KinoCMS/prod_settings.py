import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False

ALLOWED_HOSTS = ["143.198.148.29"]



SECRET_KEY = '^5_s3@w$7&_oekp!ig*1;po856-flmr338r1(_m)vc6$pat8b#'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'KinoCms',
        'USER': 'admin_cms',
        'PASSWORD': 'cmsKino2023',
        'HOST': 'localhost',
        'PORT': '5432',
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

#smtp
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'rubetsdima2004@gmail.com'
EMAIL_HOST_PASSWORD = 'gheslkacgwwucmwa'
EMAIL_PORT = 587


#CELERY settings
CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"