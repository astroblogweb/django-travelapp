from django.conf.urls import url
from . import views


app_name='infographicsresume'
urlpatterns = [

    url(r'^new', views.newresume, name='new_resume'),
    url(r'^list', views.ListResume.as_view(), name='list_resume'),
    url(r'^detail/(?P<pk>\d+)', views.DetailResume.as_view(), name='detail_resume'),
    url(r'^edit/(?P<pk>\d+)', views.edit_resume, name='edit_resume'),

    url(r'^', views.resume, name='resume'),

    # url(r'^vote/(?P<pk>\d+)',views.polls_vote,name='polls_vote'),
    # url(r'^result/(?P<pk>\d+)',views.polls_result,name='polls_result'),
]
