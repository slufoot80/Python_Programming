# Python/Django/website/music/urls.py
from django.urls import path, include
from . import views

app_name = 'music'
    # /music/
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    
    # /music/<album_id>/
    path('<pk>/', views.DetailView.as_view(), name='detail'), 

    # /music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add')
]
