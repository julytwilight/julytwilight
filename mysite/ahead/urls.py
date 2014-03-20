from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ahead.views.home.default', name='home'),
    url(r'^guy/(?P<id>\d+)/$', 'ahead.views.users.show', name='guy'),

    # login
    url(r'^whatsup/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^seeyou/$', 'django.contrib.auth.views.logout_then_login', name='logout'),

    #social
    url(r'^binding/(?P<type>\w+)/$', 'ahead.views.home.binding', name='binding'),
    url(r'^callback/(?P<type>\w+)/$', 'ahead.views.home.callback', name='callback'),

    # dream
    url(r'^', include('dreams.urls', namespace="dream")),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()