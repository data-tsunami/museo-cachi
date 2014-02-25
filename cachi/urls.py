# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',
        'cachi.views.index',
        name='index',
    ),

    url(r'^pieza/busca$',
        'cachi.views.busca_pieza',
        name='busca_pieza',
    ),
    url(r'^pieza/nueva$',
        'cachi.views.nueva_pieza',
        name='nueva_pieza',
    ),

    # url(r'^search/$',
    #     'cachi.views.search',
    #     name='search',
    # ),
    # url(r'^pieza/(?P<pk>\d+)/imagen_de_pieza/$',
    #     'cachi.views.imagen_de_pieza',
    #     name='imagen_de_pieza'
    # ),

    # Logueo y Deslogueo
    url(r'^logueo/$',
        'django.contrib.auth.views.login',
        {'template_name': 'cachi/logueo.html'},
        name="logueo"
    ),
    url(r'^deslogueo/$',
        'django.contrib.auth.views.logout',
        {'next_page': '/logueo/'},
        name="deslogueo"
    ),

    url(r'^admin/', include(admin.site.urls)),
)
