#coding: utf-8
from django.shortcuts import render
from .models import Department
from django.views.generic import ListView

class Contacts(ListView):
    model = Department     