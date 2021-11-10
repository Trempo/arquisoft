from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', csrf_exempt(views.get_paymentmethods_list), name='get_paymentmethods_list'),
    path('<int:paymentmethod_pk>/', csrf_exempt(views.paymentmethod_view), name='paymentmethod_view'),

]