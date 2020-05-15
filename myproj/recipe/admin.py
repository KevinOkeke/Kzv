from django.contrib import admin

# Register your models here.
from .models import Recipe_model, Profile_model, Comment_model, Topic_model

admin.site.register(Recipe_model)
admin.site.register(Profile_model)
admin.site.register(Comment_model)
admin.site.register(Topic_model)