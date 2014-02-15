# -*- coding: utf-8 -*-
# Django settings for cmpdelcarmen project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

MEDIA_ROOT = '/home/cilcobich/museo-cachi/media_files/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'museo-cachi_db',
        'USER': 'museo-cachi',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}