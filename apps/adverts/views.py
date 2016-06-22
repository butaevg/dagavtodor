#coding: utf-8
from .models import Advert
from django.views.generic import ListView, DetailView


class AdvertList(ListView):
    model = Advert

class AdvertDetail(DetailView):
    model = Advert