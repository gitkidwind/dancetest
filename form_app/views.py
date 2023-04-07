import datetime
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import general_contact , lesson_contact ,event_apply_detail_Form
from form_app.models import *


def contact_form(request):

    if request.method == 'POST':
        form = general_contact(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            obj = general_contact_detail(**form.cleaned_data)
            obj.save()
            return render(request, 'form_app/general_contact_form_complete.html', {'form': form})
        else:
            form = general_contact()
            return render(request, 'form_app/general_form.html', {'form': form})

    else:
        form = general_contact()

    return render(request, 'form_app/general_form.html', {'form': form})


def lesson_contact_form(request):

    if request.method == 'POST':
        form = lesson_contact(request.POST)
        if form.is_valid():
            obj = lesson_contact_detail(**form.cleaned_data)
            obj.save()
            return render(request, 'form_app/lesson_contact_form_complete.html', {'form': form})
        else:
            form = lesson_contact()

            return render(request, 'form_app/lesson_contact_form.html', {'form': form})

    else:
        form = lesson_contact()

    return render(request, 'form_app/lesson_contact_form.html', {'form': form})


# """ 送信完了画面"""
# def complete(request):
#     return render(request, 'contact/complete.html')

# def Event_Apply_Detai_form_post(request):

#     if request.method == 'POST':
#         form = lesson_contact(request.POST)
#         if form.is_valid():
#             obj = lesson_contact_detail(**form.cleaned_data)
#             obj.save()
#             return render(request, 'form_app/lesson_contact_form_complete.html', {'form': form})
#         else:
#             form = lesson_contact()

#             return render(request, 'form_app/lesson_contact_form.html', {'form': form})

#     else:
#         form = lesson_contact()

#     return render(request, 'form_app/lesson_contact_form.html', {'form': form})

def Event_Apply_Detai_form_view(request):

    form = event_apply_detail_Form(request.POST)
    return render(request, 'form_app/event_apply_detail_Form.html', {'form': form})

def Eevent_Apply_Detail_edit(request):

    form = event_apply_detail_Form(request.POST)
    return render(request, 'form_app/event_apply_detail_edit.html', {'form': form})