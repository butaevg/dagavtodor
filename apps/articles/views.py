#coding: utf-8 
from .models import Article
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ArticleMixin(object):
    model = Article
    success_url = '/articles/cp/'

    def dispatch(self, *args, **kwargs):
        return super(ArticleMixin, self).dispatch(*args, **kwargs)

class ArticleList(ArticleMixin, ListView):
    pass

class ArticleDetail(ArticleMixin, DetailView):
    pass

class ArticleCp(ArticleList):
    template_name = 'articles/article_cp.html'

class ArticleCreate(ArticleMixin, CreateView):
    fields = ['name', 'body', 'pic', 'putdate', 'source', 'source_name']

class ArticleEdit(ArticleMixin, UpdateView):
    fields = ['name', 'body', 'pic', 'putdate', 'source', 'source_name'] 

class ArticleDelete(ArticleMixin, DeleteView):
    pass