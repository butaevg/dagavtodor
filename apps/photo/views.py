#coding: utf-8
from .models import PhotoCat
from django.views.generic import ListView

class Gallery(ListView):
    model = PhotoCat 