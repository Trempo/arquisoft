from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_orderstatuses_list, name='get_orderstatuses_list'),
    path('<int:orderstatus_pk>/', views.orderstatus_view, name='orderstatus_view')
]