from django.urls import path

from . import views


urlpatterns = [

path(r'', views.index),
path('date_and_time/', views.dateAndTime, name='date_and_time')
]