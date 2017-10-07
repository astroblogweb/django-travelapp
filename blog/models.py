from django.db import models
from django import forms
#from django.forms import ModelForm
from django.utils import timezone


# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    pub_date=models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','content']