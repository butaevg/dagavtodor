#coding: utf-8
from django.http import HttpResponse
from .models import Machine
from django.contrib.auth.decorators import login_required 
from core.mixins import LoginRequiredMixin 
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView


class MachinesCp(TemplateView):
    template_name = 'machines/cp.html'


class NonworkingCp(ListView):
    queryset = Machine.objects.filter(working=0) 
    template_name = 'machines/nonworking_cp.html'

class NonworkingCreate(CreateView):
    model = Machine 
    template_name = 'machines/nonworking_form.html'
    fields = ['name', 'body', 'year_issue', 'pic_1', 'pic_2', 'pic_3', 'pic_4', 'pic_5']
    success_url = '/machines/nonworking_cp/' 

    def form_valid(self, form):
        form.instance.dep = self.request.user 
        form.instance.working = 0 
        return super(NonworkingCreate, self).form_valid(form)


class WorkingCp(ListView):
    queryset = Machine.objects.filter(working=1) 
    template_name = 'machines/working_cp.html'

class WorkingCreate(CreateView):
    model = Machine 
    template_name = 'machines/working_form.html'
    fields = ['name', 'body', 'year_issue', 'pic_1', 'pic_2', 'pic_3', 'pic_4', 'pic_5']
    success_url = '/machines/working_cp/'

    def form_valid(self, form):
        form.instance.dep = self.request.user
        return super(WorkingCreate, self).form_valid(form)


@login_required
def machine_delete(request, id):
    machine = Machine.objects.get(pk=id)
    machine.delete()
    return HttpResponse('OK')