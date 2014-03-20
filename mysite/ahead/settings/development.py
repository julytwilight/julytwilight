# -*- coding: utf-8 -*-
from ..settings import *

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'julytwilight',
        'USER': 'root',
        'PASSWORD': 'good123',
        'HOST': '',
        'PORT': '',
    }
}

# 微博
WEIBO = {
    'APP_KEY': 1951502076,
    'APP_SECRET': 'c580426fa814c46f95f3ba40d4fc904b',
    'CALLBACK_URL': 'http://127.0.0.1:8000/callback/weibo',
    'UNCALLBACK_URL': 'http://127.0.0.1:8000/cancel/weibo'
}