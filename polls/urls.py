from django.conf.urls import url
from . import views


app_name='polls'
urlpatterns = [

    url(r'^(?P<pk>\d+)', views.polls_detail, name='polls_detail'),
    #url(r'^new/$', views.blog_new, name='blog_new'),

    url(r'^vote/(?P<pk>\d+)',views.polls_vote,name='polls_vote'),
    #url(r'^vote/',views.polls_vote,name='polls_vote'),
    #url(r'^1/', views.blog_detail, name='blog_detail'),
    url(r'^', views.all_polls, name='all_polls'),
]
