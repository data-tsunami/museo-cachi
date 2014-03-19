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

from django.shortcuts import render_to_response
from django.template import RequestContext


def render_html_dinamico(request, html, contexto=None):
    if contexto == None:
        contexto = {}
    return render_to_response(
        html,
        contexto,
        context_instance=RequestContext(request)
    )


def bytes_2_mb(bytes):
    if isinstance(bytes, int):
        return float(bytes) / (1024 * 1024)
    return bytes
