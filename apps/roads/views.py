#coding: utf-8
import os
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Road, Report, ReportImg, Map, Cam3g, CamIp
from django.contrib.auth.decorators import login_required
from .forms import ReportForm, ReportImgForm

#--- Важнейшие объекты
def objects(request):
    roads = Road.objects.filter(onsite=1).filter(complete=0)
    return render(request, 'roads/objects.html', {'roads': roads})

#--- Ход работ
def progress(request, id):
    roads = Road.objects.filter(onsite=1).filter(complete=0)
    road = Road.objects.get(pk=id)
    return render(request, 'roads/progress.html', {'roads': roads, 'road': road})

@login_required
def progress_cp(request):
    roads = Road.objects.filter(onsite=1).filter(complete=0)
    return render(request, 'roads/progress_cp.html', {'roads': roads})

@login_required
def progress_reports(request, id):
    road = Road.objects.get(pk=id)
    return render(request, 'roads/progress_reports.html', {'road': road})

@login_required
def progress_report_add(request, id):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = Report(
                name = form.cleaned_data['name'],
                road_id = id)
            report.save()
            return HttpResponseRedirect('/roads/progress/reports/%s/' % id)
    else:
        form = ReportForm()
    return render(request, 'roads/progress_report_create.html', {'form': form, 'id': id})

@login_required
def progress_upload_img(request, id):
    if request.method == 'POST':
        form = ReportImgForm(request.POST, request.FILES)
        if form.is_valid():
            img = ReportImg(
                url = form.cleaned_data['pic'],
                report_id = id)
            img.save()
            return HttpResponseRedirect('/roads/progress/upload_img/%s/' % id)
    form = ReportImgForm()
    report = Report.objects.get(pk=id)
    return render(request, 'roads/progress_upload_img.html', {'form': form, 'report': report})

#--- Карты районов
def maps_list(request):
    return render(request, 'roads/maps_list.html')

def maps_detail(request, id):
    rayon = Map.objects.get(pk=id)
    return render(request, 'roads/maps_detail.html', {'rayon': rayon})

#--- Камеры
def webcam_list(request, cat):
    if cat == 'ip':
        cams = CamIp.objects.filter(hide=0)
        return render(request, 'roads/webcam_ip_list.html', {'cams': cams})
    if cat == '3g':
        #cams = Cam3g.objects.filter(hide=0)
        #return render(request, 'roads/webcam_3g_list.html', {'cams': cams})
        return HttpResponseRedirect('http://media.dagavtodor.ru/videomonitoring/gsm/')

def webcam_ip(request, id):
    cam = CamIp.objects.get(pk=id)
    return render(request, 'roads/webcam_ip_detail.html', {'cam': cam})    
