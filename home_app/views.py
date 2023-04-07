from django.shortcuts import render

# Create your views here.
def toppage(request):

    return render(request,'home_app/top.html')

def genrepage(request):

    return render(request,'home_app/genre.html')

def lesson_schedule_page(request):

    return render(request,'home_app/lesson_schedule.html')

def instructor_page(request):

    return render(request,'home_app/instructor.html')

def price_page(request):

    return render(request,'home_app/price.html')

def what_dancelive_page(request):

    return render(request,'home_app/what_dancelive.html')