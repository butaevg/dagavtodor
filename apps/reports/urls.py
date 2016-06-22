from django.conf.urls import url
from . import views 
from .views import WorkCp, WorkShow, WorkMy
from django.contrib.auth.decorators import login_required 

urlpatterns = [
	#weather
    url(r'^weather/$', views.weather),     
    url(r'^weather/my/', views.my_weather), 
    url(r'^weather/create/', views.weather_create), 
    url(r'^weather/cp/', views.weather_cp), 
    url(r'^weather/(?P<id>[0-9]+)/$', views.weather_show), 
    #work
    url(r'^work/cp/', WorkCp.as_view()),
    url(r'^work/(?P<pk>[0-9]+)/$', WorkShow.as_view()),      
    url(r'^work/my/', WorkMy.as_view()), 
    url(r'^work/create/', views.work_create),
    url(r'^work/upload_pic/(?P<id>[0-9]+)/$', views.work_upload_pic),
] 