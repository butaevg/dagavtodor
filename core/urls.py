from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.conf import settings

urlpatterns = [
    url(r'^$', include('pages.urls')), 
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^webcam/', include('camera.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^docs/', include('docs.urls')), 
    url(r'^dep(?P<id>[0-9]+)/$', include('orgs.urls')),
    url(r'^orgs/', include('orgs.urls')), 
    url(r'^instagram/', include('instagram.urls')), 
    url(r'^machines/', include('machines.urls')),
    url(r'^maps/', include('maps.urls')),
    url(r'^orders/', include('orders.urls')),
    url(r'^page/', include('pages.urls')),  
    url(r'^psd/', include('psd.urls')),
    url(r'^reports/', include('reports.urls')), 
    url(r'^roads/', include('roads.urls')), 
    url(r'^user/', include('users.urls')), 
    url(r'^workbook/', include('workbook.urls')), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()