"""travelapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin,auth
from . import views



from django.conf.urls import url,include
from fortune import views as rest_views

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', rest_views.UserViewSet)
router.register(r'groups', rest_views.GroupViewSet)






urlpatterns = [
#    url(r'^admin/logout/$','django.contrib.auth.views.logout',{'next_page': '/homepage/'}),      #views.homepage, name='homepage'),
    url(r'logout/$',views.logout_page, name='logout'),
    url(r'^analysis/',include('analysis.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^new_admin/', views.new_admin, name='new_admin'),
    url(r'^geo/',include('geopositioning.urls')),
    url(r'^geomaps/',include('geomaps.urls')),
    url(r'^fortune/',include('fortune.urls')),
    url(r'^fortune_usergroups', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),



    url(r'^places/',include('placeslist.urls')),
    url(r'^blog/',include('blog.urls')),
    url(r'^polls/',include('polls.urls')),
    url(r'^opinions/',include('opinions.urls')),
    url(r'^$',views.homepage, name='homepage'),
    url(r'^placesdata/',include('placesdata.urls')),
    url(r'^contactus/',include('contactus.urls')),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
