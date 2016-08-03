#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import News, NewsImg
from django.contrib.auth.decorators import login_required
from .forms import NewsImgForm
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from datetime import datetime


class NewsList(ListView):
    model = News

class NewsDetail(DetailView):
    model = News

class NewsCp(ListView):
    model = News
    template_name = 'news/news_cp.html'
    paginate_by = 10

@login_required
def upload_pic(request, id):
    if request.method == 'POST':
        form = NewsImgForm(request.POST, request.FILES)
        if form.is_valid():
            img = NewsImg(
                pic = form.cleaned_data['pic'],
                post_id = id)
            img.save()
            return HttpResponseRedirect('/news/upload_pic/%s/' % id)
    form = NewsImgForm()
    post = News.objects.get(pk=id)
    return render(request, 'news/news_upload_pic.html', {'form': form, 'post': post})

class NewsCreate(CreateView):
    model = News
    fields = ['name', 'source', 'body', 'mainpic', 'putdate']

class NewsEdit(UpdateView):
    model = News
    fields = ['name', 'source', 'body', 'mainpic', 'putdate']

class NewsDelete(DeleteView):
    model = News

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse("OK")