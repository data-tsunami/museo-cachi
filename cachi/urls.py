# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$',
        'cachi.views.index',
        name='index',
    ),

    url(r'^pieza/busca/$',
        'cachi.views.busca_pieza',
        name='busca_pieza',
    ),
    url(r'^pieza/nueva/$',
        'cachi.views.nueva_edita_pieza_conjunto',
        name='nueva_pieza_conjunto',
    ),
    url(r'^pieza/(?P<pieza_conjunto_pk>\d+)/$',
        'cachi.views.nueva_edita_pieza_conjunto',
        name='edita_pieza_conjunto'
    ),
    url(r'^pieza/(?P<pieza_conjunto_pk>\d+)/ficha_tecnica/nueva/$',
        'cachi.views.nueva_edita_ficha_tecnica',
        name='nueva_ficha_tecnica'
    ),
    url(r'^pieza/(?P<pieza_conjunto_pk>\d+)/ficha_tecnica/(?P<fragmento_pk>\d+)/$',
        'cachi.views.nueva_edita_ficha_tecnica',
        name='edita_ficha_tecnica'
    ),


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
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
