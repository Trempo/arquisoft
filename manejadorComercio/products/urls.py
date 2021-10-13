from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_products_list, name='get_product_list'),
    path('<int:product_pk>/', views.product_view, name='product_view')
]
