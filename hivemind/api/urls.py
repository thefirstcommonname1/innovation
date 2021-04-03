from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('/makepost', views.makepost, name='makepost'),
]