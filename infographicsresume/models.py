from django.db import models
from django import forms
from django.forms.widgets import NumberInput
from django.core.validators import MaxValueValidator, MinValueValidator


class Resume(models.Model):
    firstname=models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    dateofbirth=models.DateTimeField()
    style = models.IntegerField(default=1)
    def __str__(self):
        return self.firstname+" "+self.lastname


class DateInput(forms.DateInput):
    input_type = 'date'


class ResumeForm(forms.ModelForm):
    class Meta:
        model=Resume
        fields=['firstname','lastname','dateofbirth','style']#'__all__'
        widgets={
        'dateofbirth':DateInput(),
        'style': NumberInput(attrs={'type':'range', 'min':'1', 'max':'4'})
        }


