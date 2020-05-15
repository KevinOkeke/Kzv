from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django.core.validators import MaxValueValidator
from .models import Recipe_model, Comment_model, Topic_model, Profile_model
from . import models
class Recipe_modelForm(forms.ModelForm):
    
    class Meta:
        model = Recipe_model
        exclude = ['user']    
        # fields = ['title']
        
    
class EditProfileForm(UserChangeForm):

    class meta:
        model = User
        fields = ('first_name', 'last_name')


# class ProfileInfoForm(UserCreationForm):
#     age = forms.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
#     location = models.CharField(max_length=100, null=True, blank=True)
#     bio = models.TextField()

#     class Meta:
#         model = User
#         fields('age', 'location', 'bio')
    

class InfoForm(forms.Form):
    age = forms.IntegerField(label='Your Age')
    location = forms.CharField(label='Location', max_length=100)
    bio = forms.Textarea()

class Comment_modelForm(forms.ModelForm):

    class meta:
        model = User
        feilds = ('user', 'comment')


    
class Profile_modelForm(forms.ModelForm):

    class Meta:
        model = Profile_model
        fields = ('age', 'location', 'bio')
        # exclude = ['user']


class TopicForm(forms.Form):
    public_topic = forms.CharField(label='Topic', max_length=80)

    def save(self):
        public_topic_instance = Topic_model()
        public_topic_instance.summary = self.cleaned_data["public_topic"]
        public_topic_instance.save()
        return public_topic_instance
