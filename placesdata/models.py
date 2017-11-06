from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.

class Place(models.Model):
#    name=models.CharField(verbose_name="Place name",max_length=100)
    #site=[site_name,site_city_parent,site_link,site_rating,site_category,site_speciality]
    site_state=models.CharField(verbose_name="site_state",max_length=100)
    site_name=models.CharField(verbose_name="site_name",max_length=150,primary_key=True)
    site_city_parent=models.CharField(verbose_name="site_city_parent",max_length=50)
    site_link=models.CharField(verbose_name="site_link",max_length=200) # modified from urlfield
    site_rating=models.FloatField(verbose_name="site_rating")
    site_category=models.CharField(verbose_name="site_category",max_length=100)
    site_speciality=models.CharField(verbose_name="site_speciality",max_length=100)


class State(models.Model):
    state_name=models.CharField(verbose_name="State name",max_length=100)


class StateForm(ModelForm):
    class Meta:
        model=State
        fields = '__all__'
#		fields=['state_name']
#        widgets = { 'text': forms.Textarea(attrs={'cols': 80, 'rows': 20}),}
