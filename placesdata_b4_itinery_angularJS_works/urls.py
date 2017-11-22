from django.conf.urls import url

from . import views

app_name='placesdata'
urlpatterns = [
    # url(r'^$', views.placesdata, name='placesdata'),
    url(r'^places_scrapper', views.places_scrapper, name='places_scrapper'),
    url(r'^user_todo', views.user_todo, name='user_todo'),


    url(r'^', views.placesdata, name='placesdata'),
]
