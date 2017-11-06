from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

from .models import TravelSpotGeoMaps
from . import views

app_name='geomaps'
urlpatterns = [
#    url(r'^admin/', admin.site.urls),
    #url(r'^$', TemplateView.as_view(template_name='geomaps.html'), name='geomaps'),
    #url(r'^', TemplateView.as_view(template_name='base_geomaps_withoutdjango.html'), name='geomaps'),
    url(r'^shortlist', views.geomaps_shortlist, name='geomaps_shortlist'),
    url(r'^directions', views.geomaps_directions, name='geomaps_directions'),
    url(r'^ordering', views.geomaps_ordering, name='geomaps_ordering'),
    url(r'^sorting_rubaxa', views.geomaps_sorting_rubaxa, name='geomaps_sorting_rubaxa'),
    url(r'^reverse_geocoding',views.reverse_geocoding,name='reverse_geocoding'),
    url(r'^shortlisted_list', views.geomaps_shortlisted_display, name='geomaps_shortlisted_display'),
    url(r'^', views.geomaps, name='geomaps'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=TravelSpotGeoMaps, properties=('title', 'description', 'picture_url')), name='data')
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
