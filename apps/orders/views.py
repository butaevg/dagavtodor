#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Order
from django.contrib.auth.decorators import login_required 
from .forms import OrderExecForm


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
