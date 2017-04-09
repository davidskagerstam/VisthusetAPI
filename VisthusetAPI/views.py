from django.shortcuts import render
from django.views import generic
from django.http.response import HttpResponse

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'cafe/index.html'

class ApiView(generic.TemplateView):
    template_name = 'docs/index.html'
