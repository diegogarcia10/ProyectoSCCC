from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'html/../../templates/index.html'

class Cultivo(TemplateView):
    template_name = 'html/../../templates/cultivo.html'