from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', csrf_exempt(views.orderstatus_view.as_view()), name='get_orderstatuses_list'),
    path('<int:orderstatus_pk>/', csrf_exempt(views.orderstatus_detail_view.as_view()), name='orderstatus_view')
]