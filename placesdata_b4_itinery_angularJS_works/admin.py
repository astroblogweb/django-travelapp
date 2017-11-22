from django.contrib import admin

# Register your models here.

from . import models


admin.site.register(models.Place)
admin.site.register(models.ToDo)