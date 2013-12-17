# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'cachi.views.index', name='index'),
    url(r'^search/$', 'cachi.views.search', name='search'),
    url(r'^pieza/(?P<pk>\d+)/imagen_de_pieza/$', 'cachi.views.imagen_de_pieza',
        name='imagen_de_pieza'),

    url(r'^admin/', include(admin.site.urls)),
)
