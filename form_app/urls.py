from django.urls import path
from . import views
from form_app.views import *


app_name = 'form_app'
urlpatterns = [
    path('contact/', views.contact_form, name='contact_form'),
    path('lesson_contact/', views.lesson_contact_form, name='lesson_contact_form'),
    path('event_apply/', views.Event_Apply_Detai_form_view, name='Event_Apply_Detai_form_view'),
    path('event_apply_edit/', views.Eevent_Apply_Detail_edit, name='Eevent_Apply_Detail_edit'),



]