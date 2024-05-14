from django.urls import path, include

from . import views


urlpatterns = [
path('visitcounter/', views.numDisplay, name='numDisplay'),
path('addtwo/', views.counterDouble, name='counterDouble'),
path('reset/', views.counterReset, name='counterReset'),
path('', views.index, name='index')

]

