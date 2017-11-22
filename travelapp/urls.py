from django.conf.urls import url, include
from django.contrib import admin,auth
from . import views
from login import views as login_views
from django.contrib.auth import views as auth_views
from .settings import STATIC_ROOT, STATIC_URL
from django.conf.urls.static import static
from django.contrib.staticfiles import views as staticfiles_views

from django.conf.urls import url,include
from fortune import views as fortune_views
from placesdata import views as places_views
from travelplan import views as travelplan_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', fortune_views.UserViewSet)
router.register(r'groups', fortune_views.GroupViewSet)
router.register(r'fortune', fortune_views.FortuneViewSet)
router.register(r'places',places_views.PlaceViewSet)
router.register(r'places-travelplan',travelplan_views.PlaceViewSet)
router.register(r'travellers',travelplan_views.TravellerViewSet)#, 'travellers')
router.register(r'trips',travelplan_views.TripViewSet)#, 'trips')
router.register(r'itineraries',travelplan_views.ItineraryViewSet)#,'itineraries')


urlpatterns = [
#    url(r'^admin/logout/$','django.contrib.auth.views.logout',{'next_page': '/homepage/'}),      #views.homepage, name='homepage'),

    url(r'^analysis/',include('analysis.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^new_admin/', views.new_admin, name='new_admin'),
    url(r'^geo/',include('geopositioning.urls')),
    url(r'^geomaps/',include('geomaps.urls')),
    # url(r'^fortune/',include('fortune.urls')),
    url(r'^snippets/',include('snippets.urls')),
    url(r'^api/', include(router.urls)),      # fix needed
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # api-auth used by top right login button in API root page :P
    url(r'^infographicsresume/',include('infographicsresume.urls')),
    url(r'^asynctasks/',include('asynctasks.urls')),
    url(r'^travelplan/',include('travelplan.urls')),

    # below 'oauth removed'.. social auth incl in login screen itself
    # url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^accounts/', include('allauth.urls')),


    url(r'^blog/',include('blog.urls')),
    url(r'^polls/',include('polls.urls')),
    url(r'^opinions/',include('opinions.urls')),
    url(r'^places/',include('placeslist.urls')),
    url(r'^homepage',views.homepage, name='homepage'),  # added new
    # url(r'^angular',views.angular, name='angular'),  # added new
    url(r'^placesdata/',include('placesdata.urls')),
    url(r'^contactus/',include('contactus.urls')),
    url(r'^$',views.homepage, name='homepage'),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    #     {'document_root':STATIC_ROOT})
    url(r'^static/(?P<path>.*)$', staticfiles_views.serve),
]
# + static(STATIC_URL, document_root=STATIC_ROOT)