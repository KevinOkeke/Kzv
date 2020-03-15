from django.db import models

# Create your models here.
class Summary_Model(models.Model):
    summary = models.CharField(max_length=180)
    #title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.summary