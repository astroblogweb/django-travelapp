from django.contrib import admin

# Register your models here.

from leaflet.admin import LeafletGeoAdmin


from . import models


admin.site.register(models.TravelSpot, LeafletGeoAdmin)
