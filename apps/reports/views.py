#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Weather, WeatherCurrent, Work, WorkImg
from users.models import DUser
from roads.models import Road
from django.contrib.auth.decorators import login_required 
from core.mixins import LoginRequiredMixin 
from .forms import WeatherDateForm, WeatherForm, WorkForm, WorkImgForm
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from datetime import datetime
from core.helpers import paginate

#--- Погодные условия
def weather(request):
    if request.method == 'POST':
        form = WeatherDateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['putdate']
            df = '%d.%m.%Y'

            rows = Weather.objects.raw('SELECT * FROM reports_weather WHERE DATE_FORMAT(putdate, %s) = %s', [df, date])    
            all_list = "<a href=reports/weather/>Последние данные</a>"
            return render(request, 'reports/weather.html', {'rows': rows, 'form': form, 'all_list': all_list})
    else:
        rows = WeatherCurrent.objects.all()
        form = WeatherDateForm(initial={
            'putdate': datetime.today().strftime('%d.%m.%Y')})
    return render(request, 'reports/weather.html', {'rows': rows, 'form': form})

@login_required
def my_weather(request):
    row_list = Weather.objects.filter(rayon_id=request.user.id)
    rows = paginate(request, row_list, 4)
    return render(request, 'reports/weather_my.html', {'rows': rows})

@login_required
def weather_create(request):
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            report = Weather(
                sost = form.cleaned_data['sost'], 
                temp = form.cleaned_data['temp'], 
                pr_r = form.cleaned_data['pr_r'],
                pr_m = form.cleaned_data['pr_m'], 
                works = form.cleaned_data['works'],
                rayon_id = request.user.id)
            report.save()

            current = WeatherCurrent(
                id = request.user.id, 
                sost = form.cleaned_data['sost'], 
                temp = form.cleaned_data['temp'], 
                pr_r = form.cleaned_data['pr_r'],
                pr_m = form.cleaned_data['pr_m'], 
                works = form.cleaned_data['works'],
                rayon_id = request.user.id)
            current.save()
            return HttpResponseRedirect('/reports/weather/my/')
    else:
        wth = WeatherCurrent.objects.get(pk=request.user.id)
        form = WeatherForm(initial={
            'sost': wth.sost, 
            'temp': wth.temp, 
            'pr_r': wth.pr_r, 
            'pr_m': wth.pr_m, 
            'works': wth.works})
    return render(request, 'reports/weather_create.html', {'form': form, 'id': id})

@login_required
def weather_cp(request):
    rayons = DUser.objects.filter(cat_id=3)
    return render(request, 'reports/weather_cp.html', {'rayons': rayons})

@login_required
def weather_show(request, id):
    rayons = DUser.objects.filter(cat_id=3) 
    rayon = DUser.objects.get(pk=id)
    wth_list = Weather.objects.filter(rayon_id=id)
    wth = paginate(request, wth_list, 4)
    return render(request, 'reports/weather_show.html', {'rayons': rayons, 'rayon': rayon, 'wth': wth})


#--- Отчеты по объектам
class WorkMy(LoginRequiredMixin, TemplateView):
    template_name = 'reports/work_my.html'

    def get_context_data(self, **kwargs):
        context = super(WorkMy, self).get_context_data(**kwargs) 
        context['work_list'] = Work.objects.filter(cont=self.request.user.id)
        context['works'] = paginate(self.request, context['work_list'], 4)
        return context

@login_required
def work_upload_pic(request, id):
    if request.method == 'POST':
        form = WorkImgForm(request.POST, request.FILES)
        if form.is_valid():
            img = WorkImg(
                pic = form.cleaned_data['pic'],
                work_id = id)
            img.save()
            return HttpResponseRedirect('/reports/work/upload_pic/%s/' % id)
    form = WorkImgForm()
    imgs = WorkImg.objects.filter(work_id=id)
    return render(request, 'reports/work_upload_pic.html', {'form': form, 'imgs': imgs})

@login_required
def work_create(request):
    if request.method == 'POST':
        form = WorkForm(request.POST, user_id=request.user.id)
        if form.is_valid():
            work = Work(
                cont = request.user.id, 
                road = form.cleaned_data['road'].id,
                works = form.cleaned_data['works'],
                tech = form.cleaned_data['tech'], 
                pers = form.cleaned_data['pers'])
            work.save()
            return HttpResponseRedirect('/work/upload_pic/%d/' % work.id)
    else:
        form = WorkForm(user_id=request.user.id)
    return render(request, 'reports/work_create.html', {'form': form})


class RoadsMixin(object):
    def get_context_data(self, **kwargs):
        context = super(RoadsMixin, self).get_context_data(**kwargs)
        context['stroy'] = Road.objects.filter(cat='str', report=1) 
        context['rec'] = Road.objects.filter(cat='rec', report=1)
        context['rem'] = Road.objects.filter(cat='rem', report=1)
        return context

class WorkCp(LoginRequiredMixin, RoadsMixin, TemplateView):
    template_name = 'reports/work_cp.html'

class WorkShow(LoginRequiredMixin, RoadsMixin, DetailView):
    model = Road
    template_name = 'reports/work_show.html'

    def get_context_data(self, **kwargs):
        context = super(WorkShow, self).get_context_data(**kwargs)
        context['work_list'] = Work.objects.order_by('-putdate').filter(road=self.kwargs['pk'])
        context['works'] = paginate(self.request, context['work_list'], 4)
        return context