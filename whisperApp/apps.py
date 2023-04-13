from django.apps import AppConfig  # Import the AppConfig class from the Django apps module


class WhisperappConfig(AppConfig):  # Define a new subclass of AppConfig called 'WhisperappConfig'
    default_auto_field = "django.db.models.BigAutoField"  # Set the default auto field for this app
    name = "whisperApp"  # Set the name of the app to 'whisperApp'
