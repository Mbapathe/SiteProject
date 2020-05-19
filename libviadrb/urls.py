from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'libviadrb'

urlpatterns = [
    path('lib/', views.get_books_list, name='get_books_list'),
    path('lib/book/', views.get_book, name='get_book'),
    path('opds/', views.opds, name='opds'),
    path('opds/b/', views.opds_get_book, name='opds_get_book'),
]