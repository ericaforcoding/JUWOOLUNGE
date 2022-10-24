from django.urls import path
from . import views

app_name = 'plogging'
urlpatterns = [
  	path('', views.index, name='index')
]