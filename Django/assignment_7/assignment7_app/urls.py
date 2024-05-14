from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
path('user_form/', views.submit_user, name='submit_user'),
path('user_detail/<int:user_id>/', views.user_detail, name='user_detail'),
]