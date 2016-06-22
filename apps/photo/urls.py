from django.conf.urls import url
from .views import Gallery

urlpatterns = [
    url(r'^$', Gallery.as_view()), 
] 