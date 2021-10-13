from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_menus_list, name='get_menus_list'),
    path('<int:menu_pk>/', views.menu_view, name='menu_view'),
    path('<int:menu_pk>/products/', include('products.urls'))

]
