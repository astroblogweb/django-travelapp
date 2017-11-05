from django.db import models
from django import forms
#from django.forms import ModelForm
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    pub_date=models.DateTimeField(blank=True, null=True)
    #author=models.ForeignKey('User') #auth.User

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','content']



# Post.objects.all()
# Post.objects.create(author=me, title='Sample title', text='Test')
# from django.contrib.auth.models import User
# User.objects.all()
# me = User.objects.get(username='admin')
# Post.objects.filter(author=me)
# Post.objects.filter(title__contains='title')
# post = Post.objects.get(title="Sample title")
# post.publish()
# Post.objects.order_by('-created_date')
# Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')


