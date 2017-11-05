from django.conf.urls import url
from . import views


app_name='opinions'
urlpatterns = [

    url(r'^(?P<pk>\d+)/detail', views.Opinions_Detail.as_view(), name='opinions_detail'),
    url(r'^(?P<pk>\d+)/vote',views.opinions_vote,name='opinions_vote'),
    url(r'^(?P<pk>\d+)/result',views.Opinions_Result.as_view(),name='opinions_result'),
    url(r'^', views.Opinions_List.as_view(), name='all_opinions'),
]
