from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^my/', views.my_orders), 
    url(r'^exec/(?P<id>[0-9]+)/$', views.order_exec), 
    url(r'^$', views.order_list), 
    url(r'^(?P<id>[0-9]+)/$', views.order_detail),
] 