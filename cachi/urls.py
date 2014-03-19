# -*- coding: utf-8 -*-
#======================================================================
#    This file is part of "Museo-Cachi".
#
#    Museo-Cachi is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Museo-Cachi is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Museo-Cachi.  If not, see <http://www.gnu.org/licenses/>.
#======================================================================

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
    url(r'^pieza/(?P<pieza_conjunto_pk>\d+)/fragmento/$',
        'cachi.views.nueva_edita_fragmento',
        name='nuevo_fragmento'
    ),
    url(r'^pieza/(?P<pieza_conjunto_pk>\d+)/fragmento/(?P<fragmento_pk>\d+)/$',
        'cachi.views.nueva_edita_fragmento',
        name='edita_fragmento'
    ),
    url(r'^pieza/(?P<pieza_conjunto_pk>\d+)/fragmento/(?P<fragmento_pk>\d+)/ficha_tecnica/(?P<ficha_tecnica_pk>\d+)/$',
        'cachi.views.nueva_edita_fragmento',
        name='ver_ficha_tecnica_diagnostico'
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
