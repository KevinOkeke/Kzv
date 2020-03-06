from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")
    #return HttpResponse("CINS465 Hello World")

def about(request):
    return render(request, "about.html")
    
