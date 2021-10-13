from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_order_view, name='list_order_view'),
    path('id/<int:pk>/', views.order_view, name='order_view'),
    path('id/<int:order_pk>/items/', include('orderitems.urls'))

]