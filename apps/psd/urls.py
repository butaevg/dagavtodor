from django.conf.urls import url
from . import views 
from .views import PsdCp
from django.contrib.auth.decorators import login_required 

urlpatterns = [
	url(r'^my/', views.my_psd), 
    url(r'^exec/(?P<id>[0-9]+)/$', views.psd_exec), 
    url(r'^', PsdCp.as_view()), 
] 