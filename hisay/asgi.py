"""
ASGI config for ChatAPI project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter, ProtocolTypeRouter
from channels.security.websocket import AllowedHostsOriginValidator , OriginValidator # new
from django.core.asgi import get_asgi_application
from chat import routing  # new
# from .tokenauth_middleware import TokenAuthMiddleware  # new

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hisay.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(URLRouter(routing.websocket_urlpatterns)),
        # ['https://hisay.pythonanywhere.com', 'http://127.0.0.1:8000']
})
