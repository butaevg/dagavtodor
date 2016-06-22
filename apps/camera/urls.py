from django.conf.urls import url
from . import views 
from .views import CamIpList, CamIpDetail

urlpatterns = [
    url(r'^ip/$', CamIpList.as_view()), 
    url(r'^ip/(?P<pk>[0-9]+)/$', CamIpDetail.as_view()), 
    url(r'^3g/$', views.webcam_3g), 
] 