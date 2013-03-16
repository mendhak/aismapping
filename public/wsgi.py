import os, sys

#path = '/home/mendhak/flickrsignature'
#if path not in sys.path:
#    sys.path.append(path)

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

