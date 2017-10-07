from django.db import models
from django import forms

# Create your models here.
class Polls(models.Model):
    question=models.CharField(max_length=200)
    def __str__(self):
        return self.question

class Choice(models.Model):
    choice=models.ForeignKey(Polls,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class PollsForm(forms.ModelForm):
    class Meta:
        model=Polls
        fields='__all__'


