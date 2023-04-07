"""
WSGI config for dancemovie project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from wsgi_basic_auth import BasicAuth

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dancemovie.settings')

application = get_wsgi_application()

application = BasicAuth(application)