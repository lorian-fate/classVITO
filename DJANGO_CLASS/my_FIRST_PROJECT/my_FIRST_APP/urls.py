from django.contrib import admin
from django.urls import path
from my_FIRST_APP import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sss', views.my_map, name="my_map"),
    path('alldea', views.allDEA, name="alldea"),
    path('closestdea', views.closestDEA, name="closestDEA"),
]