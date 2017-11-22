from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User, AbstractUser



class Traveller(models.Model):
    traveller=models.ForeignKey(User)
    followers = models.ManyToManyField(
        'self',related_name='followees', symmetrical=False, blank=True,null=True)
    # followers = models.ManyToManyField('self',related_name='followees', symmetrical=False)
    def __str__(self):
        return self.traveller.username


class Trip(models.Model):
    author = models.ForeignKey(Traveller, related_name='trips')
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title
    # class Meta:
    #     unique_together = ('title', 'order')
    #     order_by = 'order'
    # def __unicode__(self):
    #     return 'Trip:\"%s\" by %s' % (self.title, self.author)

# class TripImages(models.Model):
#     post = models.ForeignKey(Trip, related_name='tripimages')
#     image = models.ImageField(upload_to="%Y/%m/%d")


class Itinerary(models.Model):
    spot = models.ForeignKey(Trip, related_name='itinerary')
    title = models.CharField(max_length=255) # to be imported from the Places API
    # body = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title

# # ex: user: SampleUser, Trip: Trip to rajasthan (Jaip+Udai+Jais),
# # TripImages: image of JM, image of fort, ..,
# # Itinerary: jm->fort1->museum1->lake->museum2..(from api)



