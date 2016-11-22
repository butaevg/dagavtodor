#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Psd
from users.models import DUser
from django.contrib.auth.decorators import login_required 
from core.mixins import LoginRequiredMixin 
from .forms import PsdExeForm
from django.views.generic import ListView


@login_required
def my_psd(request):
    roads = Psd.objects.filter(contractor=request.user.id)
    return render(request, 'psd/my.html', {'roads': roads})

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
            road.save(update_fields=['price', 'exe', 'getsum', 'exe_perc', 'exe_getsum', 'updated_at', ])
            return HttpResponseRedirect('/psd/my/')
    else:
        road = Psd.objects.get(pk=id)
        form = PsdExeForm(initial={
            'price': road.price, 
            'exe': road.exe, 
            'getsum': road.getsum})
    return render(request, 'psd/exec.html', {'form': form, 'road': road})

class PsdCp(LoginRequiredMixin, ListView):
    queryset = DUser.objects.filter(cat=7)
    context_object_name = 'contractors'
    template_name = 'psd/cp.html' 