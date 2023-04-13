import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from whisperApp.routing import websocket_urlpatterns
from whisperApp.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_mallu.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(websocket_urlpatterns)
})

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
]