
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'df2aa257fb8cf470aa3263da5d5a01af2',
        'HOST': '198.11.228.49',
        'PORT': '5433',
        'USER': 'ua3d69973664d481d9b700a0fa763bb64',
        'PASSWORD': 'p5d13bda864234463adf757b8c3474371'
    }
}
