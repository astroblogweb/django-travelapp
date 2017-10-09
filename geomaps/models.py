from djgeojson.fields import PolygonField, PointField
from django.db import models


class TravelSpotGeoMaps(models.Model):
    geom = PointField()
    description = models.TextField()
    picture = models.ImageField()

    @property
    def popupContent(self):
      return '<img src="{}" /><p><{}</p>'.format(
          self.picture.url,
          self.description)


class Shortlist(models.Model):
    # edit field types...
    val=models.TextField()
    lat=models.TextField()
    lng=models.TextField()
    location=models.TextField()
    formatted_address=models.TextField()
    sitelabel=models.TextField()
    placeid=models.TextField()
    order=models.IntegerField()