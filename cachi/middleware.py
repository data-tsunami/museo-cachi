# -*- coding: utf-8 -*-

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
