from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

#for displaying 'HomePage' on the website.
class HomePageView(TemplateView):
    template_name = 'home.html'

#for displaying About Page in the webpage.
class AboutPageView(TemplateView):
    template_name = 'about.html'

