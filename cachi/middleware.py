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

from django.contrib import auth
from django.contrib.auth.models import User


class AutomaticLoginUserMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated():
            return
        if not request.path_info.startswith('/admin'):
            return

        try:
            User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        except:
            pass

        user = auth.authenticate(username='admin', password='admin')
        if user:
            request.user = user
            auth.login(request, user)
