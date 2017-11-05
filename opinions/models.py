from django.db import models
from django import forms


class Opinions(models.Model):
    question=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    choice=models.ForeignKey(Opinions,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class ChoicessForm(forms.ModelForm):
    class Meta:
        model=Opinions
        fields='__all__'


