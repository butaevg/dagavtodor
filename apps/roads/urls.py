from django.conf.urls import url
from . import views 
from .views import (MapList, MapDetail, RoadList, RoadDetail, RoadProgressCp, 
    RoadProgressCreate, RoadProgressImg, CamIpList, CamIpDetail) 
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #maps
    url(r'^maps/$', MapList.as_view()), 
    url(r'^maps/(?P<pk>[0-9]+)/$', MapDetail.as_view()), 
    #roads
	url(r'^$', RoadList.as_view()), 
    url(r'^progress/(?P<pk>[0-9]+)/$', RoadDetail.as_view()), 
    url(r'^progress/cp/', RoadProgressCp.as_view()), 
    url(r'^progress/reports/(?P<pk>[0-9]+)/$', login_required(RoadDetail.as_view(template_name = 'roads/road_progress_reports.html'))),
    url(r'^progress/report_add/(?P<pk>[0-9]+)/$', RoadProgressCreate.as_view(template_name = 'roads/road_progress_create.html')), 
    url(r'^progress/upload_img/(?P<pk>[0-9]+)/$', RoadProgressImg.as_view(template_name = 'roads/road_progress_upload_img.html')), 
    #camera
    url(r'^webcam/ip/$', CamIpList.as_view()), 
    url(r'^webcam/ip/(?P<pk>[0-9]+)/$', CamIpDetail.as_view()), 
    url(r'^webcam/3g/$', views.webcam_3g), 
] 