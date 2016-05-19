from django.conf.urls import url
from . import views
from .views import (PostList, PostDetail, PostCp, PostCreate, 
    PostEdit, PostDelete, AdvertList, AdvertDetail, ArticleList, 
    ArticleDetail, ArticleCp, ArticleCreate, ArticleEdit, ArticleDelete, 
    QuestionList, QuestionCreate, QuestionSuccess, QuestionCp, QuestionEdit, QuestionDelete, Gallery)
from django.contrib.auth.decorators import login_required
from .yandex import YandexRSS

urlpatterns = [
    #adverts
    url(r'^adverts/$', AdvertList.as_view()), 
    url(r'^advert/(?P<pk>[0-9]+)/$', AdvertDetail.as_view()), 
	#news
    url(r'^post/(?P<pk>[0-9]+)/$', PostDetail.as_view(), name='news-item'), 
    url(r'^newsarchive/$', PostList.as_view()), 
    url(r'^news/cp/', login_required(PostCp.as_view())), 
    url(r'^post/create/', login_required(PostCreate.as_view())),
    url(r'^post/edit/(?P<pk>[0-9]+)/$', login_required(PostEdit.as_view())),
    url(r'^post/upload_pic/(?P<id>[0-9]+)/$', views.upload_pic),
    url(r'^post/delete/(?P<pk>[0-9]+)/$', login_required(PostDelete.as_view())),
    url(r'^rss/', YandexRSS()), 
    #articles
    url(r'^articles/$', ArticleList.as_view()), 
    url(r'^article/(?P<pk>[0-9]+)/$', ArticleDetail.as_view()), 
    url(r'^articles/cp/', login_required(ArticleCp.as_view())),
    url(r'^article/create/', login_required(ArticleCreate.as_view())),
    url(r'^article/edit/(?P<pk>[0-9]+)/$', login_required(ArticleEdit.as_view())),
    url(r'^article/delete/(?P<pk>[0-9]+)/$', login_required(ArticleDelete.as_view())),
    #faq
    url(r'^questions/$', QuestionList.as_view()), 
    url(r'^question/create/', QuestionCreate.as_view()),
    url(r'^question/success/', QuestionSuccess.as_view()), 
    url(r'^questions/cp/', login_required(QuestionCp.as_view())),     
    url(r'^question/edit/(?P<pk>[0-9]+)/$', login_required(QuestionEdit.as_view())), 
    url(r'^question/showhide/(?P<id>[0-9]+)/(?P<hide>[0-9]+)/$', views.question_showhide),
    url(r'^question/delete/(?P<pk>[0-9]+)/$', login_required(QuestionDelete.as_view())), 
    #photo
    url(r'^photo/$', Gallery.as_view()), 
] 