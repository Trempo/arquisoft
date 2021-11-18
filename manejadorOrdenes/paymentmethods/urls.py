from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', csrf_exempt(views.paymentmethods_view.as_view()), name='get_paymentmethods_list'),
    path('<int:paymentmethod_pk>/', csrf_exempt(views.paymentmethodsdetail_view.as_view()), name='paymentmethod_view'),

]