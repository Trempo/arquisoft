from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_menus_list, name='get_menus_list'),
    path('id/<int:pk>/', views.menu_view, name='menu_view')

]
