# -*- coding: utf-8 -*-
from ..settings import *

DEBUG = False

TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'secret',
        'USER': 'root',
        'PASSWORD': 'Agood123',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['julytwilight.com', 'www.julytwilight.com']

# 微博
WEIBO = {
    'APP_KEY': 2934779440,
    'APP_SECRET': '94e3b4568884821c34aca5164638f78c',
    'CALLBACK_URL': 'http://julytwilight.com/callback/weibo',
    'UNCALLBACK_URL': 'http://julytwilight.com/uncallback/weibo'
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
