from django.conf.urls import url
from . import views 
from .views import MachinesCp, MachineCreate, MachinesWorkingCp, MachineWorkingCreate
from django.contrib.auth.decorators import login_required

urlpatterns = [
	#orders
    url(r'^orders/my/', views.my_orders), 
    url(r'^orders/exec/(?P<id>[0-9]+)/$', views.order_exec), 
    url(r'^orders/$', views.order_list), 
    url(r'^order/(?P<id>[0-9]+)/$', views.order_detail),
    #psd
    url(r'^psd/my/', views.my_psd), 
    url(r'^psd/exec/(?P<id>[0-9]+)/$', views.psd_exec), 
    url(r'^psd/', views.psd), 
    #weather
    url(r'^weather/$', views.weather),     
    url(r'^weather/my/', views.my_weather), 
    url(r'^weather/create/', views.weather_create), 
    url(r'^weather/cp/', views.weather_cp), 
    url(r'^weather/(?P<id>[0-9]+)/$', views.weather_show), 
    #work
    url(r'^work/cp/', views.work_cp),
    url(r'^work/(?P<id>[0-9]+)/$', views.work_show),      
    url(r'^work/my/', views.my_work), 
    url(r'^work/create/', views.work_create),
    url(r'^work/upload_pic/(?P<id>[0-9]+)/$', views.work_upload_pic),
    #instagram
    url(r'^instagram/$', views.instagram), 
    #machines 
    url(r'^machines/cp/', login_required(MachinesCp.as_view())),  
    url(r'^machines/create/', login_required(MachineCreate.as_view())),
    url(r'^machines_working/cp/', login_required(MachinesWorkingCp.as_view())), 
    url(r'^machines_working/create/', login_required(MachineWorkingCreate.as_view())),
    url(r'^machines_working/machine_delete/(?P<id>[0-9]+)/$', views.machine_delete),
] 