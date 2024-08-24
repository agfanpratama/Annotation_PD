from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('job', views.job, name='job'),
    path('notification', views.notifications, name='notifications'),
    path('data-image', views.data_image, name='data_image'),
    path('issues', views.issues, name='issues'),
    path('overview', views.overview, name='overview'),


]