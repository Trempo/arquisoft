from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', csrf_exempt(views.orderitem_view.as_view()), name='get_orderitems_list'),
    path('<int:orderitem_pk>/', csrf_exempt(views.orderitem_detail_view.as_view()), name='orderitem_view')
]
