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
from login import views as login_views
from django.contrib.auth import views as auth_views


from django.conf.urls import url,include
from fortune import views as rest_views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', rest_views.UserViewSet)
router.register(r'groups', rest_views.GroupViewSet)






urlpatterns = [
#    url(r'^admin/logout/$','django.contrib.auth.views.logout',{'next_page': '/homepage/'}),      #views.homepage, name='homepage'),

    url(r'^analysis/',include('analysis.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^new_admin/', views.new_admin, name='new_admin'),
    url(r'^geo/',include('geopositioning.urls')),
    url(r'^geomaps/',include('geomaps.urls')),
    url(r'^fortune/',include('fortune.urls')),
    url(r'^fortune_usergroups/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^infographicsresume/',include('infographicsresume.urls')),



    #url(r'^login/',include('login.urls')),

    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^register/$',login_views.UserFormView.as_view(),name='register'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^accounts/', include('allauth.urls')),
    # above 'oauth removed'.. social auth incl in login screen itself
    # url(r'logout/$',views.logout_page, name='logout'),



    url(r'^blog/',include('blog.urls')),
    url(r'^polls/',include('polls.urls')),
    url(r'^opinions/',include('opinions.urls')),
    url(r'^places/',include('placeslist.urls')),
    url(r'^homepage',views.homepage, name='homepage'),  # added new
    url(r'^placesdata/',include('placesdata.urls')),
    url(r'^contactus/',include('contactus.urls')),
    url(r'^$',views.homepage, name='homepage'),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
