from django.conf.urls import url,include
from . import views
from rest_framework import routers


app_name='fortune'


# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet, base_name='user-detail')
# router.register(r'groups', views.GroupViewSet) #, base_name='fortune')


urlpatterns = [
    url(r'^$', views.FortuneList.as_view(), name='fortune_list'),
    url(r'^fortuneapi', views.FortuneAPIList.as_view(), name='fortune_api-list'),

    #url(r'^', include(router.urls))    #,name='fortuneapi_users'),



    #url(r'^usersrest/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #url(r'^places_scrapper', views.places_scrapper, name='places_scrapper'),
]


# : tutorial / app: quickstart
# : travelapp / app: fortune