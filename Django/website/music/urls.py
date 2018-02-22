# Python/Django/website/music/urls.py
from django.urls import path, include
from . import views

app_name = 'music'
    # /music/
urlpatterns = [
    path('', views.index, name='index'),
    
    # /music/<album_id>/
    path('<int:album_id>/', views.detail, name='detail'), 

    # /music/<album_id>/favorite
    path('<int:album_id>/favorite', views.detail, name='favorite'), 

]
