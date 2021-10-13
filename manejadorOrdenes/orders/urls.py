from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_order_view, name='list_order_view'),
    path('<int:order_pk>/', views.order_view, name='order_view'),
    path('<int:order_pk>/orderitems/', include('orderitems.urls'))

]