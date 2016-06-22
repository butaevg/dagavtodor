from django.conf.urls import url
from .views import (ArticleList, ArticleDetail, ArticleCp, ArticleCreate, 
    ArticleEdit, ArticleDelete)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', ArticleList.as_view()), 
    url(r'^(?P<pk>[0-9]+)/$', ArticleDetail.as_view()), 
    url(r'^cp/', login_required(ArticleCp.as_view())),
    url(r'^create/', login_required(ArticleCreate.as_view())),
    url(r'^edit/(?P<pk>[0-9]+)/$', login_required(ArticleEdit.as_view())),
    url(r'^delete/(?P<pk>[0-9]+)/$', login_required(ArticleDelete.as_view())), 
] 