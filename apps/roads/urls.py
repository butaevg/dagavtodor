from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.objects), 
	#progress
    url(r'^progress/(?P<id>[0-9]+)/$', views.progress), 
    url(r'^progress/cp/', views.progress_cp), 
    url(r'^progress/reports/(?P<id>[0-9]+)/$', views.progress_reports), 
    url(r'^progress/report_add/(?P<id>[0-9]+)/$', views.progress_report_add), 
    url(r'^progress/upload_img/(?P<id>[0-9]+)/$', views.progress_upload_img), 
    #maps
    url(r'^maps/$', views.maps_list), 
    url(r'^maps/(?P<id>[0-9]+)/$', views.maps_detail), 
    #camera
    url(r'^webcam/(?P<cat>[\w-]+)/$', views.webcam_list), 
    url(r'^webcam/ip/(?P<id>[0-9]+)/$', views.webcam_ip), 
    #url(r'^webcam/3g/(?P<id>[0-9]+)/$', views.webcam_3g), 
] 