#coding: utf-8
import os
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Road, Report, ReportImg
from django.contrib.auth.decorators import login_required 
from core.mixins import LoginRequiredMixin
from .forms import ReportImgForm
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#--- Важнейшие объекты (ход работ)
class RoadList(ListView):
    queryset = Road.objects.filter(onsite=1).filter(complete=0)

class RoadDetail(DetailView):
    model = Road

    def get_context_data(self, **kwargs):
        context = super(RoadDetail, self).get_context_data(**kwargs)
        context['roads'] = Road.objects.filter(onsite=1).filter(complete=0)
        return context

class RoadProgressCp(LoginRequiredMixin, ListView):
    queryset = Road.objects.filter(onsite=1).filter(complete=0) 
    context_object_name = 'roads'
    template_name = 'roads/road_progress_cp.html' 


class RoadProgressCreate(LoginRequiredMixin, CreateView):
    model = Report 
    fields = ['name']

    def form_valid(self, form):
        form.instance.road_id = self.kwargs['pk']
        return super(RoadProgressCreate, self).form_valid(form)

class RoadProgressImg(LoginRequiredMixin, CreateView):
    model = ReportImg 
    fields = ['url']

    def get_context_data(self, **kwargs):
        context = super(RoadProgressImg, self).get_context_data(**kwargs)
        context['report'] = Report.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.report_id = self.kwargs['pk']
        return super(RoadProgressImg, self).form_valid(form)