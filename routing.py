from django.urls import path
from django.conf.urls import url, include
from channels.routing import ProtocolTypeRouter, URLRouter
from whisperApp.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": URLRouter([
        path("", include("whisperApp.urls")),
    ]),
    "websocket": URLRouter(
        websocket_urlpatterns
    )
})
