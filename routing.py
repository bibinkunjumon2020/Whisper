from django.urls import path
from django.conf.urls import include
from channels.routing import ProtocolTypeRouter, URLRouter
from whisperApp.routing import websocket_urlpatterns


# Define the application's routing protocol based on the request type
application = ProtocolTypeRouter({
    # If the request is an HTTP request,
    "http": URLRouter([
        # Route the request to the included URLs in whisperApp/urls.py
        path("", include("whisperApp.urls")),
    ]),
    # If the request is a WebSocket request,
    "websocket": URLRouter(
        # Route the request to the URLs defined in whisperApp/routing.py
        websocket_urlpatterns
    )
})