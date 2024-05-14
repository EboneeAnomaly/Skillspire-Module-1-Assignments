from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_page, name='course_page'),
    path('courses/', views.course_page, name='course_page'),
    path('courses/add/', views.add_course, name='add_course'),
    path('courses/delete/<int:course_id>/', views.delete_course, name='delete_course'),
]