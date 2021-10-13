from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_comercio_view, name='list_comercio_view'),
    path('<int:comercio_pk>/', views.comercio_view, name='comercio_view'),
    path('<int:comercio_pk>/menus/', include('menus.urls'))

]
