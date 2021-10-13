from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_paymentmethods_list, name='get_paymentmethods_list'),
    path('<int:paymentmethod_pk>/', views.paymentmethod_view, name='paymentmethod_view'),

]