import os
import sys

path = '/srv/www'
if path not in sys.path:
	sys.path.append('srv/www')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

