from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('pages.urls')), 
    url(r'^adverts/', include('adverts.urls')), 
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^articles/', include('articles.urls')), 
    url(r'^webcam/', include('camera.urls')),
    url(r'^contacts/', include('contacts.urls')), 
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^docs/', include('docs.urls')), 
    url(r'^faq/', include('faq.urls')), 
    url(r'^oad/', include('oad.urls')), 
    url(r'^orgs/', include('orgs.urls')), 
    url(r'^instagram/', include('instagram.urls')), 
    url(r'^machines/', include('machines.urls')),
    url(r'^maps/', include('maps.urls')),
    url(r'^news/', include('news.urls')), 
    url(r'^pressa/', include('news.urls')),
    url(r'^orders/', include('orders.urls')),
    url(r'^page/', include('pages.urls')),  
    url(r'^psd/', include('psd.urls')),
    url(r'^reports/', include('reports.urls')), 
    url(r'^roads/', include('roads.urls')), 
    url(r'^photo/', include('photo.urls')),
    url(r'^user/', include('users.urls')), 
]
