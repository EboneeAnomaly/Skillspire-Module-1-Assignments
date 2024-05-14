from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('destination/', views.destination_page, name='destination_page'),
    path('travels/', views.travels_page, name='travels_page'),
    path('add_trip/', views.add_trip_page, name='add_trip_page'),
    path('add_trip/', views.add_trip, name='add_trip'),
]
