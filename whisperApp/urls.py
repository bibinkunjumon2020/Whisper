
from django.urls import path  # Import the 'path' function from Django's URL framework.
from .views import ChatView  # Import the ChatView class from the 'views.py' module in the same directory as this file.

# Define a list of URL patterns for this web application.
urlpatterns = [
    path('', ChatView.as_view(), name='chat'),  # Map the root URL to the ChatView class using the 'as_view' method and give it the name

]