#coding: utf-8
from django.http import HttpResponseRedirect, HttpResponse
from .models import Question
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class QuestionList(ListView):
    queryset = Question.objects.filter(hide=0)
    paginate_by = 4

class QuestionCreate(CreateView):
    model = Question
    fields = ['name', 'city', 'address', 'email', 'msg', 'img']
    success_url = '/faq/success/'

class QuestionSuccess(TemplateView):
    template_name = 'faq/question_success.html'

class QuestionCp(ListView):
    model = Question
    template_name = 'faq/question_cp.html'
    paginate_by = 4

class QuestionEdit(UpdateView):
    model = Question
    fields = ['msg', 'answer']
    template_name = 'faq/question_edit_form.html'
    success_url = '/faq/cp/'

@login_required
def question_showhide(request, id, hide):
    post = Question(
        id = id, 
        hide = int(hide))
    post.save(update_fields=['hide',])
    return HttpResponseRedirect('/faq/cp/')

class QuestionDelete(DeleteView):
    model = Question

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponse("OK")