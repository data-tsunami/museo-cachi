#!/usr/bin/python

import os, sys

_PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#_PROJECT_NAME = _PROJECT_DIR.split('/')[-1]
_PROJECT_NAME = 'cachi'
_PROJECT_USR = _PROJECT_DIR.split('/')[-3]

virtualenv = '/home/%s/virtualenv/env_piopablodiaz/bin/activate_this.py' % _PROJECT_USR 
execfile(virtualenv, dict(__file__=virtualenv))

sys.path.insert(0, _PROJECT_DIR)
sys.path.insert(0, os.path.dirname(_PROJECT_DIR))

os.environ['DJANGO_SETTINGS_MODULE'] = "%s.settings" % _PROJECT_NAME

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")