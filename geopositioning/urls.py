'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^', views.geo, name='geo'),
]
'''


from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

from .models import TravelSpot


urlpatterns = [
#    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='geo.html'), name='geo'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=TravelSpot, properties=('title', 'description', 'picture_url')), name='data')
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
