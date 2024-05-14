from django.urls import path
from . import views


urlpatterns = [

path(r'', views.submitPost, name='submit'),
path('post/', views.submitPost, name='submit_post'),

]