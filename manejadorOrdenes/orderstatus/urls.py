from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_orderstatuses_list, name='get_orderstatuses_list'),
    path('id/<int:pk>/', views.orderstatus_view, name='order_view')

]