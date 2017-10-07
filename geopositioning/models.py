'''
from django.db import models

# Create your models here.

from geoposition.fields import GeopositionField

class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()
'''
from djgeojson.fields import PolygonField, PointField
from django.db import models


class TravelSpot(models.Model):
    '''
    title = models.CharField(max_length=256)
    description = models.TextField()
    picture = models.ImageField()
    geom = PolygonField()

    def __unicode__(self):
        return self.title

    @property
    def picture_url(self):
        return self.picture.url
    '''
    geom = PointField()
    description = models.TextField()
    picture = models.ImageField()

    @property
    def popupContent(self):
      return '<img src="{}" /><p><{}</p>'.format(
          self.picture.url,
          self.description)
