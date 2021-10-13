from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.menus_view, name='menus_view'),
    path('id/<int:pk>/', views.menu_view, name = 'menu_view')

]

