from django.conf.urls import url
from . import views
from .views import (NewsList, NewsDetail, NewsCp, NewsCreate, 
    NewsEdit, NewsDelete)
from django.contrib.auth.decorators import login_required
from .yandex import YandexRSS

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', NewsDetail.as_view(), name='news-item'), 
    url(r'^archive/$', NewsList.as_view()), 
    url(r'^cp/', login_required(NewsCp.as_view())), 
    url(r'^create/', login_required(NewsCreate.as_view())),
    url(r'^edit/(?P<pk>[0-9]+)/$', login_required(NewsEdit.as_view())),
    url(r'^upload_pic/(?P<id>[0-9]+)/$', views.upload_pic),
    url(r'^delete/(?P<pk>[0-9]+)/$', login_required(NewsDelete.as_view())),
    url(r'^rss/', YandexRSS()), 
] 