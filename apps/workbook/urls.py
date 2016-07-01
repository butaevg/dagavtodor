from django.conf.urls import url
from . import views 
from views import WorkCp, WorkShow

urlpatterns = [     
    url(r'^my/', views.my), 
    url(r'^create/', views.create), 
    url(r'^cp/', WorkCp.as_view()), 
    url(r'^show/(?P<pk>[0-9]+)/$', WorkShow.as_view()), 
] 