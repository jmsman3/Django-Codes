from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("THis is first Home pge")

def courses(request):
    return HttpResponse("this is First page/Courses")

def about(request):
    return HttpResponse("this is first apge/ about")


# Create your views here.
