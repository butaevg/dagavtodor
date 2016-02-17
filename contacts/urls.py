from django.conf.urls import url
from . import views
from views import Contacts

urlpatterns = [
    url(r'^$', Contacts.as_view()), 
] 