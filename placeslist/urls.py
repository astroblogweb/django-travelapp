from django.conf.urls import url

from . import views

app_name='placeslist'
urlpatterns = [
    url(r'^', views.welcome, name='welcome'),
]
