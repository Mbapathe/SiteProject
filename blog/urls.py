from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('', views.me, name='me'),
	path('projects/', views.projects, name='projects'),
	path('blog/', views.blog, name='blog'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
