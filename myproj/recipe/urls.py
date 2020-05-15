#from django.contrib import admin
from django.urls import path, include



from . import views


urlpatterns = [
    
    path('', views.homepage_view, name='home'),
    path('personal/', views.personal_view, name='personal'),
    path('create/', views.create_user_view, name='create'),
    path('recipes/', views.choose_recipe_view, name='recipes'),
    path('howto/<int:pk>/', views.how_to_views, name='howto'),
    path('popular/', views.popular_recipe_view, name='popular'),
    path('guests/', views.guestpage_view, name='guests'),
    path('profile/', views.my_profile_view, name='profile'),
    path('make/', views.make_recipe_view, name='makerecipe'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    
    
    
    # path('recipe_new/', views.personal_view, name='personal')
    
    # path('', include("myproj.urls")),
 ]