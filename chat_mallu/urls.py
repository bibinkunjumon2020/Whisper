from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from whisperApp.views import ChatView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ChatView.as_view(), name='chat'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
