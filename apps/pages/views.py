#coding: utf-8
from django.shortcuts import render
from .models import Page
from news.models import News
from django.views.generic import DetailView

def mainpage(request):
    posts = News.objects.order_by('-putdate')[:3]
    return render(request, 'pages/mainpage.html', {'posts': posts})

class PageDetail(DetailView):
    model = Page