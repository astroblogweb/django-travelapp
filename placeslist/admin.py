#from django.contrib import admin

# Register your models here.

from django import forms
from django.contrib import admin

from easy_maps.widgets import AddressWithMapWidget

'''
from .models import Firm

class FirmAdmin(admin.ModelAdmin):
    class form(forms.ModelForm):
        class Meta:
            widgets = {
                'address': AddressWithMapWidget({'class': 'vTextField'})
            }

admin.site.register(Firm, FirmAdmin)
'''
