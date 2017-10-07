from django.conf.urls import url

from . import views
from .views import ChartData,HomeView

app_name='analysis'
urlpatterns = [
    url(r'^charts_func/', views.get_data, name='charts'),
    url(r'^api/data/', views.get_data_api_data, name='api-data'),
    url(r'^api/charts/data/', ChartData.as_view()),
    url(r'^home_view/', HomeView.as_view()),
    url(r'^', views.analysis, name='analysis'),
]
