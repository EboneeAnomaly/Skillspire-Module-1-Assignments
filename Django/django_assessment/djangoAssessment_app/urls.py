from django.urls import path

from . import views


urlpatterns = [
path('greeting/', views.greeting),
path('greeting/<str:firstname>/', views.greeting, name='greeting'),
path('djangoInfo/', views.infoPage),
path('greet/<str:name>/', views.personalGreeting),
path('contact/', views.contact, name='contact'),
path('confirmation/', views.confirmation, name= 'confirmation'),
path('login/', views.login, name='login'),
path('admin/', views.admin, name='admin'),
path('', views.index),

]