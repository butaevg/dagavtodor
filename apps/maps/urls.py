from django.conf.urls import url
from .views import MapList, MapDetail 

urlpatterns = [
    url(r'^$', MapList.as_view()), 
    url(r'^(?P<pk>[0-9]+)/$', MapDetail.as_view()), 
] 