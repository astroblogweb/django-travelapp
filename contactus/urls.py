from django.conf.urls import url

from . import views

app_name='contactus'
urlpatterns = [
    url(r'^$', views.email, name='email'),
    url(r'^email/', views.email, name='email'),
    url(r'^success/', views.success, name='success'),
]
