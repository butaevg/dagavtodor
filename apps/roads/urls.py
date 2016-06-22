from django.conf.urls import url
from . import views 
from .views import (RoadList, RoadDetail, RoadProgressCp, 
    RoadProgressCreate, RoadProgressImg) 
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^$', RoadList.as_view()), 
    url(r'^progress/(?P<pk>[0-9]+)/$', RoadDetail.as_view()), 
    url(r'^progress/cp/', RoadProgressCp.as_view()), 
    url(r'^progress/reports/(?P<pk>[0-9]+)/$', login_required(RoadDetail.as_view(template_name = 'roads/road_progress_reports.html'))),
    url(r'^progress/report_add/(?P<pk>[0-9]+)/$', RoadProgressCreate.as_view(template_name = 'roads/road_progress_create.html')), 
    url(r'^progress/upload_img/(?P<pk>[0-9]+)/$', RoadProgressImg.as_view(template_name = 'roads/road_progress_upload_img.html')), 
] 