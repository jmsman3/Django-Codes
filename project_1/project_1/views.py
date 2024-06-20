from django.http import HttpResponse

def home(request):
    return HttpResponse("THis is HOme Page")

def contact(request):
    return HttpResponse("this is Contact Page")
