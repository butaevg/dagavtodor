#coding: utf-8
from .models import Map
from django.views.generic import ListView, DetailView 


class MapList(ListView):
    model = Map

class MapDetail(DetailView):
    model = Map