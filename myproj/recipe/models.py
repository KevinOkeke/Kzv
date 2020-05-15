from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator


# Create your models here.
class Recipe_model(models.Model):
    title = models.CharField(max_length=180, null=True, blank=True)
    description = models.TextField(default='Enter a description here', null=True, blank=True)
    ingredients = models.TextField(default='Enter ingredients here', null=True, blank=True)
    cook_time = models.PositiveIntegerField(validators=[MaxValueValidator(720)])
    servings = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(20)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='recipe/image', blank=True, null=True, default='noimage.png')
    directions = models.TextField(default="Enter cooking instructions here", null=True, blank=True)
    

    def __str__(self):
        return self.title        

   

class Topic_model(models.Model):
    public_topic = models.CharField(max_length=100)

    def __str__(self):
        return self.public_topic


class Comment_model(models.Model):
    comment = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.comment


class Profile_model(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()



    