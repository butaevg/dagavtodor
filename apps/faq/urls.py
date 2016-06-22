from django.conf.urls import url
from . import views
from .views import (QuestionList, QuestionCreate, QuestionSuccess, 
    QuestionCp, QuestionEdit, QuestionDelete)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', QuestionList.as_view()), 
    url(r'^create/', QuestionCreate.as_view()),
    url(r'^success/', QuestionSuccess.as_view()), 
    url(r'^cp/', login_required(QuestionCp.as_view())),     
    url(r'^edit/(?P<pk>[0-9]+)/$', login_required(QuestionEdit.as_view())), 
    url(r'^showhide/(?P<id>[0-9]+)/(?P<hide>[0-9]+)/$', views.question_showhide),
    url(r'^delete/(?P<pk>[0-9]+)/$', login_required(QuestionDelete.as_view())),  
] 