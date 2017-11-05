from django.db import models
#from django.forms import ModelForm
#from django import forms

class Fortune(models.Model):
    position=models.IntegerField(default=1)
    name=models.CharField(max_length=150,primary_key=True)
    value=models.IntegerField(default=1000)

    def __str__(self):
        return self.name