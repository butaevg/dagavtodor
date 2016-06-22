#coding: utf-8
from django.shortcuts import render
from .models import Insta
from django.contrib.auth.decorators import login_required 
from datetime import datetime

def instagram(request):
    deps = Insta.objects.all()
    day, month = (datetime.today().strftime('%d'), datetime.today().strftime('%m'))
    return render(request, 'instagram/index.html', {'deps': deps, 'day': day, 'month': month})
