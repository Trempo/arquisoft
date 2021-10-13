from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_paymentmethods_list, name='get_paymentmethods_list'),
    path('id/<int:pk>/', views.paymentmethod_view, name='paymentmethod_view')

]