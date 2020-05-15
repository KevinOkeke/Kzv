"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static


#from webpages.views import homepage_view #Better way might need to use later
#from webpages import views
#from recipe.views import homepage_views, personal_view, create_user_view, how_to_views, popular_recipe_view, guestpage_view
#from webpages import views as create_user_view
#from recipe import views


urlpatterns = [
    #path('',homepage_view),  # better way might need to use later
    path('chat/', include('chat.urls')),
    path('', include('recipe.urls')),
    # path('', views.homepage_view, name='home'),
    # path('personal/', views.personal_view, name='personal'),
    # path('create/', views.create_user_view, name='create'),
    # path('recipes/', views.choose_recipe_view, name='recipes'),
    # path('howto/', views.how_to_views, name='howto'),
    # path('popular/', views.popular_recipe_view, name='popular'),
    # path('guests/', views.guestpage_view, name='guests'),
    # path('accounts/', include('django.contrib.auth.urls')), #django authentication files    
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
