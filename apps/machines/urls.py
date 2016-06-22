from django.conf.urls import url
from . import views 
from .views import MachinesCp, NonworkingCp, NonworkingCreate, WorkingCp, WorkingCreate
from django.contrib.auth.decorators import login_required 

urlpatterns = [
	url(r'^cp/', login_required(MachinesCp.as_view())), 
    url(r'^nonworking_cp/', login_required(NonworkingCp.as_view())),  
    url(r'^nonworking_create/', login_required(NonworkingCreate.as_view())), 
    url(r'^working_cp/', login_required(WorkingCp.as_view())), 
    url(r'^working_create/', login_required(WorkingCreate.as_view())),
    url(r'^delete/(?P<id>[0-9]+)/$', views.machine_delete),
] 