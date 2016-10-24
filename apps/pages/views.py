#coding: utf-8
from django.shortcuts import render
from .models import Page
from reports.models import WeatherCurrent
from django.views.generic import DetailView

def mainpage(request):
    rows = WeatherCurrent.objects.all()
    return render(request, 'pages/mainpage.html', {'rows': rows})

def pages(request, section):
    pages = Page.objects.filter(section=section).order_by('id')
    pages_sec = pages[0].section
    return render(request, 'pages/page_list.html', {'pages': pages, 'pages_sec': pages_sec})

class PageDetail(DetailView):
    model = Page

class BDD(PageDetail):
    template_name = 'pages/bdd.html'