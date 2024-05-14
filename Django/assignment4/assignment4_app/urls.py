from django.urls import path

from . import views


urlpatterns = [
    path('info-index.html', views.infoIndex, name='info-index'),
    path('info-form.html', views.infoForm, name='info-form'), 
    path('form-data.html', views.formData, name='form-data'),
    path(r'', views.index, name='index')

]   