from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import models
from . import forms

def index(request):
    if request.method == "POST":
        form = forms.NameForm(request.POST)
        if form.is_valid():
            form.save()
            form = forms.NameForm()
    else:
        form = forms.NameForm()
    summary_info = models.Summary_Model.objects.all()

    variable = {
        "body":"CINS465 Hello World",
        "summary_info":summary_info,
        "form":form
        
    }
    return render(request, "index.html", context=variable)
    #return HttpResponse("CINS465 Hello World")

def about(request):
    about_variable = {
        "temp_list":range(5)
    }
    return render(request, "about.html",context=about_variable)
    
