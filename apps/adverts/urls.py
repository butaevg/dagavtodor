from django.conf.urls import url
from .views import AdvertList, AdvertDetail

urlpatterns = [
    url(r'^$', AdvertList.as_view()), 
    url(r'^(?P<pk>[0-9]+)/$', AdvertDetail.as_view()), 
] 