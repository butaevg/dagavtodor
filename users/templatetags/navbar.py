#coding: utf-8
from django import template
from users.models import Category, UserCat, DUser

#http://djbook.ru/rel1.8/howto/custom-template-tags.html#django.template.Library.inclusion_tag
register = template.Library()  

#http://stackoverflow.com/questions/29183653/wiki-render-did-not-receive-values-for-the-arguments-request
@register.inclusion_tag('navbar/navbar.html', takes_context=True)  
def show_navbar(context):
    request = context['request']
    group = UserCat.objects.get(pk=request.user.cat_id) 
    return {'group': group}