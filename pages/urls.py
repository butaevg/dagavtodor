from django.conf.urls import url
from . import views
from .views import PageDetail

urlpatterns = [
    url(r'^$', views.mainpage),
    url(r'^(?P<slug>[\w-]+)/$', PageDetail.as_view()), 
] 