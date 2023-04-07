from django.urls import path
from movie_app.views import *
from . import views

app_name = 'movie_app'
urlpatterns = [
    path('top/',views.movie_top_page, name='movie_top_page'),
    path('top/play',views.movie_play_page, name='movie_play_page'),
]
