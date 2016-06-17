#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Advert, Article, PhotoCat, Post, PostImg, Question
from django.contrib.auth.decorators import login_required
from .forms import NewsImgForm
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.dates import YearArchiveView
from datetime import datetime
from helpers.paginate import paginate 


#--- Объявления
class AdvertList(ListView):
    model = Advert

class AdvertDetail(DetailView):
    model = Advert


#--- Статьи
class ArticleList(ListView):
    model = Article

class ArticleDetail(DetailView):
    model = Article

class ArticleCp(ListView):
    model = Article
    template_name = 'pressa/article_cp.html'

class ArticleCreate(CreateView):
    model = Article
    fields = ['name', 'body', 'pic', 'putdate', 'source', 'source_name']
    success_url = '/pressa/articles/cp/'

    def get_initial(self):
        return { 'putdate': datetime.today().strftime('%d.%m.%Y') }

class ArticleEdit(UpdateView):
    model = Article
    fields = ['name', 'body', 'pic', 'putdate', 'source', 'source_name']
    success_url = '/pressa/articles/cp/'

class ArticleDelete(DeleteView):
    model = Article
    success_url = '/pressa/articles/cp/'


#--- Фотоархив
class Gallery(ListView):
    model = PhotoCat 


#--- Новости
class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class PostCp(ListView):
    model = Post
    template_name = 'pressa/post_cp.html'
    paginate_by = 10

@login_required
def upload_pic(request, id):
    if request.method == 'POST':
        form = NewsImgForm(request.POST, request.FILES)
        if form.is_valid():
            img = PostImg(
                pic = form.cleaned_data['pic'],
                post_id = id)
            img.save()
            return HttpResponseRedirect('/pressa/post/upload_pic/%s/' % id)
    form = NewsImgForm()
    post = Post.objects.get(pk=id)
    return render(request, 'pressa/post_upload_pic.html', {'form': form, 'post': post})

class PostCreate(CreateView):
    model = Post
    fields = ['name', 'source', 'body', 'mainpic', 'putdate']

    #def get_initial(self):
        #return { 'putdate': datetime.today().strftime('%d.%m.%Y') }

class PostEdit(UpdateView):
    model = Post
    fields = ['name', 'source', 'body', 'mainpic', 'putdate']

class PostDelete(DeleteView):
    model = Post

    def get(self, request, *args, **kwargs):
        return HttpResponse("OK")


#--- Обращения граждан
class QuestionList(ListView):
    queryset = Question.objects.filter(hide=0)
    paginate_by = 4

class QuestionCreate(CreateView):
    model = Question
    fields = ['name', 'city', 'address', 'email', 'msg', 'img']
    success_url = '/pressa/question/success/'

class QuestionSuccess(TemplateView):
    template_name = 'pressa/question_success.html'

class QuestionCp(ListView):
    model = Question
    template_name = 'pressa/question_cp.html'
    paginate_by = 4

class QuestionEdit(UpdateView):
    model = Question
    fields = ['msg', 'answer']
    template_name = 'pressa/question_edit_form.html'
    success_url = '/pressa/questions/cp/'

@login_required
def question_showhide(request, id, hide):
    post = Question(
        id = id, 
        hide = int(hide))
    post.save(update_fields=['hide',])
    return HttpResponseRedirect('/pressa/questions/cp/')

class QuestionDelete(DeleteView):
    model = Question

    def get(self, request, *args, **kwargs):
        return HttpResponse("OK")