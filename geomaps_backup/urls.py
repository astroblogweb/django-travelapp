from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

from .models import TravelSpotGeoMaps


app_name='geomaps'
urlpatterns = [
#    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='geomaps.html'), name='geomaps'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=TravelSpotGeoMaps, properties=('title', 'description', 'picture_url')), name='data')
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
