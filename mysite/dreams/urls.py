# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^dreams/$', "dreams.views.dream.index", name='all'),
    url(r'^dream/create/$', "dreams.views.dream.create", name='create'),
    url(r'^dream/(?P<id>\d+)/$', "dreams.views.dream.show", name='show'),
    url(r'^dream/(?P<id>\d+)/comment/$', "dreams.views.comment.create", name='comment'),
)