from django.conf.urls import url
from . import views
from django.conf import settings
#from django.views.generic import TemplateView


urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.me, name='me'),
	url(r'^me$', views.me, name='me'),
	url(r'^projects$', views.projects, name='projects'),
	url(r'^blog$', views.blog, name='blog'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]
