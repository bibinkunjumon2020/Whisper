# Importing the necessary libraries for this code
from django.shortcuts import render
from django.views.generic import TemplateView

# Defining a class named ChatView which inherits TemplateView class 
class ChatView(TemplateView):
    # Setting the template name to be rendered by this view
    template_name = 'chat.html'
