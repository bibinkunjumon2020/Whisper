import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from whisperApp.routing import websocket_urlpatterns
from whisperApp.consumers import ChatConsumer

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_mallu.settings')

# Define the application's routing protocol based on the request type
application = ProtocolTypeRouter({
    # If the request is an HTTP request, use the standard ASGI application
    "http": get_asgi_application(),
    # If the request is a WebSocket request,
    "websocket": URLRouter(websocket_urlpatterns)
})

# Define the URLs that should be routed to the ChatConsumer
websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
]
