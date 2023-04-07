from django.urls import path
from . import views
from home_app.views import *


app_name = 'home_app'
urlpatterns = [
    path('top/', views.toppage, name='toppage'),
    path('genre/', views.genrepage, name='genrepage'),
    path('lesson_schedule/', views.lesson_schedule_page, name='lesson_schedule_page'),
    path('instructor/', views.instructor_page, name='instructor_page'),
    path('price/', views.price_page, name='price_page'),
    path('what_dancelive/', views.what_dancelive_page, name='what_dancelive_page'),


]