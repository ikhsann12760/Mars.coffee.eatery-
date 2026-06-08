from django.urls import path
from . import views

app_name = 'cafe'

urlpatterns = [
    path('', views.index, name='index'),
]