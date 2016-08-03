#coding: utf-8
from django.http import HttpResponseRedirect
from .models import Cam3g, CamIp
from django.views.generic import ListView, DetailView 


def webcam_3g(request):
    return HttpResponseRedirect('http://media.dagavtodor.ru/videomonitoring/gsm/')

class CamIpList(ListView):
    queryset = CamIp.objects.filter(hide=0)

class CamIpDetail(DetailView):
    model = CamIp