from django.conf.urls import url
from . import views


app_name='asynctasks'
urlpatterns = [
    # url(r'^', views.dummy_view, name='tasks'),

    url(r'taskdone/', views.TaskdoneListView.as_view(), name='taskdone'),
    url(r'^', views.GenerateRandomUserView.as_view(), name='tasks'),
]
