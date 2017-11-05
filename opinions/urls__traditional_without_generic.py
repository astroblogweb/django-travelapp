from django.conf.urls import url
from . import views


app_name='opinions'
urlpatterns = [

    url(r'^detail/(?P<pk>\d+)', views.opinions_detail, name='opinions_detail'),
    #url(r'^new/$', views.blog_new, name='blog_new'),

    url(r'^vote/(?P<pk>\d+)',views.opinions_vote,name='opinions_vote'),
    url(r'^result/(?P<pk>\d+)',views.opinions_result,name='opinions_result'),
    #url(r'^vote/',views.opinions_vote,name='opinions_vote'),
    #url(r'^1/', views.blog_detail, name='blog_detail'),
    url(r'^', views.all_opinions, name='all_opinions'),
]
