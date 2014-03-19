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

"""
WSGI config for cachi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cachi.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
