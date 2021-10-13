from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_orderitems_list, name='get_orderitems_list'),
    path('<int:orderitem_pk>/', views.orderitem_view, name='orderitem_view')
]
