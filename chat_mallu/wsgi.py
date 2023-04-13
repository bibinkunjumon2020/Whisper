# Import the necessary modules for serving the Django application
import os
from django.core.wsgi import get_wsgi_application

# Set the environment variable to point to the project's settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat_mallu.settings")

# Retrieve the WSGI application object configured for this project
application = get_wsgi_application()

