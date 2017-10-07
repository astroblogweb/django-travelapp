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
