#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Org, Info, Dep
from users.models import DUser
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

def show(request, cat):
    orgs = Org.objects.filter(cat=cat).order_by('name')
    orgs_type = orgs[0].get_cat_display()
    return render(request, 'orgs/show.html', {'orgs': orgs, 'orgs_type': orgs_type})

def pv(request):
    uch = Org.objects.filter(cat='uch').order_by('-name')
    pre = Org.objects.filter(cat='pre').order_by('name')
    ao = Org.objects.filter(cat='ao').order_by('name')
    dep = Org.objects.filter(cat='dep').order_by('name')
    return render(request, 'orgs/pv.html', {'uch': uch, 'pre': pre, 'ao': ao, 'dep': dep})

class OrgDetail(DetailView):
    model = Org

@login_required
def depinfo(request, org_id, cat):
	orgs = DUser.objects.filter(cat=3)
	org = DUser.objects.get(pk=org_id)
	dep = Info.objects.filter(org_id=org_id, cat=cat).first()
	return render(request, 'orgs/depinfo.html', {'orgs': orgs, 'org': org, 'dep': dep, 'cat': cat})

def dep(request, id):
    org = DUser.objects.get(id=id)
    try:
        org_info = Dep.objects.get(dep_id=id)
    except Dep.DoesNotExist:
        org_info = None
    return render(request, 'orgs/dep_mainpage.html', {'org': org, 'org_info': org_info})