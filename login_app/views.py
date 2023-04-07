from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from login_app.models import *
from login_app.forms import *

# Create your views here.

def signin(request):

    if request.method == "GET":
        return render(request, 'login_app/login.html')

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        login(request, user)
        return HttpResponseRedirect(reverse('home_app:toppage'), {'user': user})
    else:
        return render(request, 'login_app/login.html', {'error_message': 'login failed'})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home_app:toppage'))


@login_required
def user_detail(request):
    user_obj = MyUser.objects.get(pk=request.user.id)
    print(user_obj)
    return render(request, 'login_app/user_detail.html', {'user': user_obj})

@login_required
def user_edit_detail(request):
    user_obj = MyUser.objects.get(pk=request.user.id)
    
    initial_values = {
                "id":user_obj.id,
                "email": user_obj.email, 
                "first_name": user_obj.first_name,
                "last_name": user_obj.last_name,
                "first_kana": user_obj.first_kana,
                "last_kana": user_obj.last_kana,
                "number_of_student": user_obj.number_of_student
                }
    if request.method == 'POST':

        form = MyUser_Form(request.POST or initial_values)
        
        if form.is_valid():
            
            if user_obj.email == form.cleaned_data['email']:
                form.cleaned_data.pop('email')

            obj = MyUser(**form.cleaned_data)
            obj.save()
            form = MyUser.objects.get(pk=request.user.id)

            return redirect("login_app:user_detail") #render(request, 'login_app/user_detail.html', {'form': form})
        else:
            form = MyUser_Form(initial_values)

            return render(request, 'login_app/user_edit_detail.html', {'form': form})

    else:
        form = MyUser_Form(initial_values)


        return render(request, 'login_app/user_edit_detail.html', {'form': form})


