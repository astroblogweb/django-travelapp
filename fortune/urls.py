from django.conf.urls import url,include
from . import views
from rest_framework import routers


app_name='fortune'


urlpatterns = [
    url(r'^$', views.FortuneList.as_view(), name='fortune_list'),
    url(r'^fortuneapi', views.FortuneAPIList.as_view(), name='fortune_api-list'),
    url(r'^fortuneapilist_template', views.FortuneAPIList.as_view(), name='fortune_api-list-template'),
    url(r'^fortuneapidetail_template', views.FortuneAPIDetail.as_view(), name='fortune_api-detail-template'),
]

