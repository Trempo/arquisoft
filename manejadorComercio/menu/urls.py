from django.contrib import admin
from django.urls import path
from . import views

ulrpatterns = [
    path('', views.menus_view, name='menus_view'),
    path('<int:pk>', views.menu_view, name = 'menu_view')

]

