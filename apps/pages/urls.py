from django.conf.urls import url
from . import views
from .views import PageDetail, BDD

urlpatterns = [
    url(r'^$', views.mainpage),
    url(r'^(?P<section>[0-9]+)/$', views.pages), 
    url(r'^bdd/(?P<slug>[\w-]+)/$', BDD.as_view()), 
    url(r'^(?P<slug>[\w-]+)/$', PageDetail.as_view()), 
] 