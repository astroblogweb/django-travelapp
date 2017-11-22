from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Traveller)
admin.site.register(models.Trip)
admin.site.register(models.Itinerary)