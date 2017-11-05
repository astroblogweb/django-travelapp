from django.db import models
from django import forms
# import floppyforms
from django.forms.widgets import NumberInput
from django.core.validators import MaxValueValidator, MinValueValidator

class Resume(models.Model):
    firstname=models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    dateofbirth=models.DateTimeField()
#    style = models.IntegerField(default=1,validators=[MaxValueValidator(10),MinValueValidator(1)])
    # below line works as validator
    #style = models.IntegerField(default=1,validators=[MaxValueValidator(10),MinValueValidator(1)])
    style = models.IntegerField(default=1)
    def __str__(self):
        return self.firstname+" "+self.lastname
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# class Choice(models.Model):
#     choice=models.ForeignKey(Polls,on_delete=models.CASCADE)
#     choice_text=models.CharField(max_length=200)
#     votes=models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text

class DateInput(forms.DateInput):
    input_type = 'date'


# class RangeInput(NumberInput):
#     input_type = 'range'
#     min= -10
#     max=10
#     attrs={'min': 5, 'max': 20}


# class Slider(floppyforms.RangeInput):
#     min=1
#     max=5
#     step=1
#     template_name = 'slider.html'

#     class Media:
#         js = (
#             'js/jquery.min.js',
#             'js/jquery-ui.min.js',
#         )
#         css = {
#             'all': (
#                 'css/jquery-ui.css',
#             )
#         }


class ResumeForm(forms.ModelForm):
    class Meta:
        model=Resume
        fields=['firstname','lastname','dateofbirth','style']#'__all__'
        widgets={
        'dateofbirth':DateInput(),
        'style': NumberInput(attrs={'type':'range', 'min':'1', 'max':'10'})
        }


