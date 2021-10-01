from django.shortcuts import render
from .logic.menu_logic import *
from django.http import HttpResponse
from django.core import serializers


def menus_view(request):
    if request.method == 'GET':
        menus = get_menus()
        menus_dto = serializers.serialize('json', menus)
        return HttpResponse(menus_dto, 'application/json')


def menu_view(request, pk):
    if request.method == 'GET':
        menu = get_menu(pk)
        menu_dto = serializers.serialize('json', menu)
        return HttpResponse(menu_dto, 'application/json')


