#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import DUser
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    mess = ''
    if ('username' in request.REQUEST) and ('password' in request.REQUEST):
        username = request.REQUEST['username']
        password = request.REQUEST['password']
        user = authenticate(username=username, password=password)        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            mess = 'Неверный логин или пароль!'
    form = LoginForm()
    return render(request, 'users/login.html', {'form': form, 'mess': mess})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def cp(request):
    return render(request, 'users/cp.html')