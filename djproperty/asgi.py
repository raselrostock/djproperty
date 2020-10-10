"""
ASGI config for djproperty project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djproperty.settings.production')

application = get_asgi_application()
