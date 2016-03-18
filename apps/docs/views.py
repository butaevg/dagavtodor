#coding: utf-8
from django.shortcuts import render
from .models import DocsCat, Doc

def index(request, id=1):
    cats = DocsCat.objects.order_by('-id').all() 
    docs = Doc.objects.filter(cat=id).order_by('-id')
    return render(request, 'docs/index.html', {'cats': cats, 'docs': docs})