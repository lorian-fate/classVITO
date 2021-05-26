from os import name
from django.contrib import admin
from django.urls import path
from my_FIRST_APP import views

urlpatterns = [
    path('', views.home, name="home"),
    path('closest/', views.closest_DEA, name="closest"),
    path('listdea/', views.list_DEA, name='listdea'),
    
    #path('sss', views.my_map, name="my_map"),
    path('user/', views.user_ubication, name="user_pos"),
    path('log/', views.log_user, name="log_user"),
    path("api/", views.my_api),
    path('api/<codigo>/', views.solo_dea),
]