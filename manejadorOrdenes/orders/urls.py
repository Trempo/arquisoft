from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', csrf_exempt(views.order_view.as_view()), name='list_order_view'),
    path('<int:order_pk>/', csrf_exempt(views.order_detail_view.as_view()), name='order_view'),
    path('<int:order_pk>/orderitems/', include('orderitems.urls'))

]