from django.urls import re_path  # Import the 're_path' function from Django's URL framework.
from . import consumers  # Import the ChatConsumer class defined in the 'consumers.py' module.

# Define a list of URL patterns for WebSocket connections.
websocket_urlpatterns = [
    re_path(r'ws/chat/$', consumers.ChatConsumer.as_asgi()),  # Match any WebSocket connections to the '/ws/chat/' path with the ChatConsumer class.
]
