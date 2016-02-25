#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Insta, Order, OrderExec, Psd, Weather, WeatherCurrent, Work, WorkImg, Machine
from users.models import DUser
from roads.models import Road
from django.contrib.auth.decorators import login_required
from .forms import OrderExecForm, PsdExeForm, WeatherDateForm, WeatherForm, WorkForm, WorkImgForm
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView
from datetime import datetime
from helpers.paginate import paginate

class MachinesCp(ListView):
    model = Machine
    template_name = 'reports/machine_cp.html'

class MachineCreate(CreateView):
    model = Machine
    fields = ['name', 'body', 'year_issue', 'pic_1']
    success_url = '/reports/machines/cp/'

    def form_valid(self, form):
        form.instance.dep = self.request.user
        return super(MachineCreate, self).form_valid(form)

# @login_required
# def machine_create(request):
#     if request.method == 'POST':
#         form = MachineForm(request.POST, request.FILES)
#         if form.is_valid():
#             mach = Machine(                
#                 name = form.cleaned_data['name'],
#                 body = form.cleaned_data['body'],
#                 year_issue = form.cleaned_data['year_issue'], 
#                 pic_1 = form.cleaned_data['pic_1'], 
#                 dep_id = request.user.id)
#             mach.save()
#             return HttpResponseRedirect('/machines/cp/')
#     else:
#         form = MachineForm()
#     return render(request, 'reports/machine_create.html', {'form': form})


def instagram(request):
    deps = Insta.objects.all()
    day, month = (datetime.today().strftime('%d'), datetime.today().strftime('%m'))
    return render(request, 'reports/instagram.html', {'deps': deps, 'day': day, 'month': month})

#--- Поручения
@login_required
def my_orders(request):
    orders = Order.objects.filter(members=request.user.id)
    return render(request, 'reports/orders_my.html', {'orders': orders})

@login_required
def order_exec(request, id):
    rep = OrderExec.objects.filter(order_id=id, member_id=request.user.id).first()
    if rep == None:        
        if request.method == 'POST':
            form = OrderExecForm(request.POST)
            if form.is_valid():
                report = OrderExec(
                    process = form.cleaned_data['process'], 
                    process_perc = form.cleaned_data['process_perc'], 
                    member_id = request.user.id, 
                    order_id = id)
                report.save()
                return HttpResponseRedirect('/reports/orders/my/')
        else:
            order = Order.objects.get(pk=id)
            form = OrderExecForm()
        return render(request, 'reports/orders_exec.html', {'form': form, 'order': order})
    else:
        if request.method == 'POST':
            form = OrderExecForm(request.POST)
            if form.is_valid():
                report = OrderExec(
                    id = rep.id,
                    process = form.cleaned_data['process'], 
                    process_perc = form.cleaned_data['process_perc'])
                report.save(update_fields=['process', 'process_perc', ])
                return HttpResponseRedirect('/reports/orders/my/')
        else:
            order = Order.objects.get(pk=id)
            form = OrderExecForm(initial={
                    'process': rep.process, 
                    'process_perc': rep.process_perc})
        return render(request, 'reports/orders_exec.html', {'form': form, 'order': order})


@login_required
def order_list(request):
    orders = Order.objects.filter(hide=0)
    return render(request, 'reports/order_list.html', {'orders': orders})

@login_required
def order_detail(request, id):
    order = Order.objects.get(pk=id)
    rows = OrderExec.objects.filter(order_id=id)
    return render(request, 'reports/order_detail.html', {'order': order, 'rows': rows})

#--- ПСД
@login_required
def my_psd(request):
    roads = Psd.objects.filter(contractor=request.user.id)
    return render(request, 'reports/psd_my.html', {'roads': roads})

@login_required
def psd_exec(request, id):
    if request.method == 'POST':
        form = PsdExeForm(request.POST)
        if form.is_valid():
            price = float(form.cleaned_data['price'])
            exe = float(form.cleaned_data['exe'])
            getsum = float(form.cleaned_data['getsum'])
            road = Psd(
                id = id, 
                price = price, 
                exe = exe, 
                getsum = getsum, 
                exe_perc = round((exe/price)*100), 
                exe_getsum = round((getsum/price)*100))
            road.save(update_fields=['price', 'exe', 'getsum', 'exe_perc', 'exe_getsum', ])
            return HttpResponseRedirect('/reports/psd/my/')
    else:
        road = Psd.objects.get(pk=id)
        form = PsdExeForm(initial={
            'price': road.price, 
            'exe': road.exe, 
            'getsum': road.getsum})
    return render(request, 'reports/psd_exec.html', {'form': form, 'road': road})

@login_required
def psd(request):
    pr1 = Psd.objects.filter(contractor=121)
    pr2 = Psd.objects.filter(contractor=123)
    pr3 = Psd.objects.filter(contractor=124)
    pr4 = Psd.objects.filter(contractor=125)
    return render(request, 'reports/psd.html', {'pr1': pr1, 'pr2': pr2, 'pr3': pr3, 'pr4': pr4})


#--- Погодные условия
def weather(request):
    if request.method == 'POST':
        form = WeatherDateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['putdate']
            df = '%d.%m.%Y'

            rows = Weather.objects.raw('SELECT * FROM reports_weather WHERE DATE_FORMAT(putdate, %s) = %s', [df, date])    
            all_list = "<a href=reports/weather/>Весь список</a>"
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
@login_required
def my_work(request):
    work_list = Work.objects.filter(cont=request.user.id)
    works = paginate(request, work_list, 4)
    return render(request, 'reports/work_my.html', {'works': works})

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

@login_required
def work_cp(request):
    stroy = Road.objects.filter(cat='str', report=1)
    rec = Road.objects.filter(cat='rec', report=1)
    rem = Road.objects.filter(cat='rem', report=1)
    return render(request, 'reports/work_cp.html', {'stroy': stroy, 'rec': rec, 'rem': rem})

@login_required
def work_show(request, id):
    stroy = Road.objects.filter(cat='str', report=1)
    rec = Road.objects.filter(cat='rec', report=1)
    rem = Road.objects.filter(cat='rem', report=1)
    road = Road.objects.get(pk=id)
    work_list = Work.objects.order_by('-putdate').filter(road=id)
    works = paginate(request, work_list, 4)
    return render(request, 'reports/work_show.html', {'stroy': stroy, 'rec': rec, 'rem': rem, 'road': road, 'works': works})
