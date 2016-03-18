from django.conf.urls import url
from . import views
from .views import OrgDetail

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', OrgDetail.as_view()),
    url(r'^pv/$', views.pv),
    url(r'^(?P<cat>[\w-]+)/$', views.show), 
    url(r'^depinfo/(?P<org_id>[0-9]+)/(?P<cat>[0-9]+)/$', views.depinfo),
] 