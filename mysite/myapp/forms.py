from django import forms

from . import models

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

    def save(self):
        your_name_instance = models.Summary_Model()
        your_name_instance.summary = self.cleaned_data["your_name"]
        your_name_instance.save()
        return your_name_instance