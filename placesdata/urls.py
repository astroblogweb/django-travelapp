from django.conf.urls import url

from . import views

app_name='placesdata'
urlpatterns = [
    url(r'^$', views.placesdata, name='placesdata'),
    url(r'^places_scrapper', views.places_scrapper, name='places_scrapper'),
]
