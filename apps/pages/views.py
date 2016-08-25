#coding: utf-8
from django.shortcuts import render
from .models import Page
from news.models import News
from django.views.generic import DetailView

def mainpage(request):
    posts = News.objects.order_by('-putdate')[:3]
    return render(request, 'pages/mainpage.html', {'posts': posts})

def pages(request, section):
    pages = Page.objects.filter(section=section).order_by('id')
    pages_sec = pages[0].section
    return render(request, 'pages/page_list.html', {'pages': pages, 'pages_sec': pages_sec})

class PageDetail(DetailView):
    model = Page

class BDD(PageDetail):
    template_name = 'pages/bdd.html'