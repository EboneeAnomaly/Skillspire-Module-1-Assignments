from django.urls import path

from . import views


urlpatterns = [
path('display-name.html', views.displayName, name='display_name'),
path('favorite-food.html', views.favoriteFood, name='favorite_food'),
path('favorite-vacation.html', views.favoriteVacation, name='favorite_vacation'),

path(r'', views.index)

]