from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from .forms import Recipe_modelForm, Profile_modelForm, TopicForm, Comment_modelForm, InfoForm
from .models import Recipe_model, Profile_model, Comment_model, Topic_model


from . import models




# Create your views here.
def homepage_view(request, *args, **kwargs): #request
        #print(request.user) 
        #return HttpResponse("<h1>Recipes & things</h1>")
        obj = Recipe_model.objects.all()

        my_context = {
                "my_recipe": "Recent Recipes",
                "my_total": 245,
                "fav_recipe": ["chocolate", "lemon", "pie"],
                "home_header" : "Cook with the book",
                "obj":obj,
                "count":range(5)                
                
                
        }
        return render(request, "home.html", my_context)

def create_user_view(request, *args, **kwargs):
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()       
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')                     
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "create.html/", {'form': form})
       

@login_required
def choose_recipe_view(request, *args, **kwargs): 
               
        myrecipes = Recipe_model.objects.all()
                    
        context = {
        'myrecipes': myrecipes,
        
        }
        return render(request, "recipes.html", context=context)


@login_required
def how_to_views(request, pk, *args, **kwargs):

        recipe_instr = get_object_or_404(Recipe_model, pk=pk)
       
        
        return render(request, "howto.html", {'recipe_instr':recipe_instr})


@login_required
def popular_recipe_view(request, *args, **kwargs):

        all_model = Recipe_model.objects.all
        find_u = Recipe_model

                   

        return render(request, "popular.html", {})

def guestpage_view(request, *args, **kwargs):

        if request.method == "POST":
                form = forms.TopicForm(request.POST)
                if form.is_valid():
                        p = Topic_model()
                        p.public_topic = form.cleaned_data['public_topic']
                        p.save()                        

        else:
                form = forms.TopicForm()
                          
        topic_info = Topic_model.objects.all()#[:5]
            
        context = {        
        'topic_info':topic_info,
        'form':form
        }
        
        return render(request, "guests.html", context=context)


def personal_view(request, *args, **kwargs):
       
       

        
        context = {
                'form':form
        }

        # rform = Recipe_modelForm(request.POST, request.FILES or None)
        # if rform.is_valid():
        #         recipe = rform.save(commit=False)
        #         recipe.user = request.user
        #         recipe.save()               
        #         # rform.save()
        
        # p_context = {'rform': rform}
        
        return render(request, "personal.html", context)

# @login_required
# def my_profile_view(request, *args, **kwargs):

#         profileform = Profile_modelForm(request.POST)
#         if profileform.is_valid():
#                 profile = profileform.save(commit=False)
#                 profile.user = request.user
#                 profile.save()               
                
        
#         profile_context = {'profileform':profileform }
                
#         return render(request, "profile.html", profile_context)


@login_required
def my_profile_view(request):

        profileform = Profile_modelForm(request.POST)        
                       
        if request.method == 'POST':
                # profileform = Profile_modelForm(request.POST, instance=request.user)
        
                if profileform.is_valid():
                        p = Profile_model()
                        profile = profileform.save(commit=False)
                        p.user = request.user
                        p.age = profileform.cleaned_data.get('age') 
                        p.location = profileform.cleaned_data.get('location')
                        p.bio = profileform.cleaned_data.get('bio')                    
                        p.save()
                        
                        
                        return redirect('profile')
        else:
                profileform = Profile_modelForm()               

        output = Profile_model    
        
        context = {
            'profileform':profileform,
            'output':output,
            
                     
        }

        
               
        return render(request, "profile.html", context)


def make_recipe_view(request, *args, **kwargs):

        rform = Recipe_modelForm(request.POST, request.FILES or None)

        if rform.is_valid():
                recipe = rform.save(commit=False)
                recipe.user = request.user
                recipe.save()               
                
                return redirect("recipes")
        
        p_context = {'rform': rform}
        
        return render(request, "makerecipe.html", p_context)


# @login_required
# def profile(request):
#         profile_updateform = Profile_modelForm

#         context = {
#                 'p_form':profile_updateform
#         }

#         return render(request, "editprofile.html", context)




# def user_recipes(request):
#         r = Recipe_modelForm()        
#         #     title = recipe_form.cleaned_data.get('title')

#         recipe_context={
#             'rform':r
#         }
#         return render(request, "personal.html", recipe_context)