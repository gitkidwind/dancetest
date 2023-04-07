from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from movie_app.models import *
# Create your views here.



@login_required
def movie_top_page(request):
    print(request.user.is_movie_subscription)
    if request.user.is_movie_subscription:
        #obj = Event_Application.objects.all()

                                                                #,{'obj':obj}
        return render(request,'movie_app/movie_top_page.html',)
    else:
        
        return render(request,'movie_app/movie_unregister.html')



@login_required
def movie_play_page(request):
    #obj = Event_Application.objects.first()


    return render(request,'movie_app/movie_play_page.html',)