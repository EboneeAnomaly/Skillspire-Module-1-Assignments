from django.urls import path
from . import views

app_name = 'assignment9_app'

urlpatterns = [
    path('', views.userPage, name='users'),
    path('users/', views.userPage, name='users'),
    path('users/add/', views.addUser, name='add_user'),
    path('users/create/', views.createUser, name='create_user'),
]