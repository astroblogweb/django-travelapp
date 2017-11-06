from django.conf.urls import url
from . import views


app_name='blog'
urlpatterns = [

    url(r'^(?P<pk>\d+)/$', views.blog_detail, name='blog_detail'),
    url(r'^new/$', views.blog_new, name='blog_new'),
    url(r'^edit/(?P<pk>\d+)/$', views.blog_edit, name='blog_edit'),
    url(r'^$', views.blog_list, name='blog_list'),

    #url(r'^1/', views.blog_detail, name='blog_detail'),
]


# "{% url 'post_new' %}"