# Import the necessary modules for defining URL patterns and serving media files
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Import the ChatView class from the whisperApp.views module
from whisperApp.views import ChatView

# Define the URL patterns for the app
urlpatterns = [
    # Route requests to the /admin/ URL to the Django admin site
    path('admin/', admin.site.urls),
    # Route requests to the root URL to the ChatView class, named 'chat'
    path('', ChatView.as_view(), name='chat'),
]

# Serve media URL patterns in development mode only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
