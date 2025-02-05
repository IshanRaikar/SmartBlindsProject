from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from SmartBlindsProjectApp import models

# Create your views here.
class HomeView(TemplateView):
    template_name = 'testwebpage.html'