"""
WSGI config for djproperty project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djproperty.settings.production')

application = get_wsgi_application()
