#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Workbook
from users.models import DUser
from django.contrib.auth.decorators import login_required 
from core.mixins import LoginRequiredMixin 
from .forms import WorkbookForm
from django.views.generic import DetailView, TemplateView


@login_required
def my(request):
    work_list = Workbook.objects.filter(dep=request.user.id)
    #works = paginate(request, work_list, 4)
    return render(request, 'workbook/my.html', {'work_list': work_list})

@login_required
def create(request):
    if request.method == 'POST':
        form = WorkbookForm(request.POST, request.FILES, user_id=request.user.id)
        if form.is_valid():
            work = Workbook(
                dep_id = request.user.id, 
                road_id = form.cleaned_data['road'].id,
                file = form.cleaned_data['file'],
                putdate = form.cleaned_data['putdate'])
            work.save()
            return HttpResponseRedirect('/workbook/my/')
    else:
        form = WorkbookForm(user_id=request.user.id)
    return render(request, 'workbook/create.html', {'form': form})

class OrgsMixin(object):
    def get_context_data(self, **kwargs):
        context = super(OrgsMixin, self).get_context_data(**kwargs)
        context['orgs'] = DUser.objects.filter(cat=3) 
        return context

class WorkCp(LoginRequiredMixin, OrgsMixin, TemplateView):
    template_name = 'workbook/cp.html'

class WorkShow(LoginRequiredMixin, OrgsMixin, DetailView):
    model = DUser
    template_name = 'workbook/show.html'

    def get_context_data(self, **kwargs):
        context = super(WorkShow, self).get_context_data(**kwargs)
        context['work_list'] = Workbook.objects.order_by('-putdate').filter(dep=self.kwargs['pk'])
        #context['works'] = paginate(self.request, context['work_list'], 4)
        return context