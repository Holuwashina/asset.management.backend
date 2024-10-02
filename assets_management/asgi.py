"""
ASGI config for assets_management project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

settings_module = 'assets_management.deployment_settings' if 'RENDER_EXTERNAL_HOSTNAME' in os.environ else 'assets_management.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_asgi_application()
