from django.urls import path
from . import views
from login_app.views import *

app_name = 'login_app'
urlpatterns = [
    path('login/', views.signin, name='login'),
    path('logout/', views.user_logout, name='user_logout'),

    path('user_detail/', views.user_detail, name='user_detail'),
    path('user_edit_detail/', views.user_edit_detail, name='user_edit_detail'),



]