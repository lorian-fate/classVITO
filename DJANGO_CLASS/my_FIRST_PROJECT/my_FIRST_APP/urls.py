from os import name
from django.contrib import admin
from django.urls import path
from my_FIRST_APP import views

urlpatterns = [
    path('', views.home, name="home"),
    path('closest/', views.closestDEA, name="closest"),
    path('sss', views.my_map, name="my_map"),
    path('user/', views.user_ubication, name="user_pos")
]