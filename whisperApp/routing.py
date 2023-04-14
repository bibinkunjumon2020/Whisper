from django.urls import re_path  
from . import consumers  
# Define a list of URL patterns for WebSocket connections.
websocket_urlpatterns = [
    re_path(r'ws/chat/$', consumers.ChatConsumer.as_asgi()),  # Match any WebSocket connections to the '/ws/chat/' path with the ChatConsumer class.
]                           #its similar to rest url making
