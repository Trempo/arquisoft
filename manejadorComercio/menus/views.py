from django.core.serializers import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .logic.menu_logic import *
from django.http import HttpResponse
from django.core import serializers


def get_menus_list(request):
    if request.method == 'GET':
        menus = get_menus()
        menus_dto = serializers.serialize('json', menus)
        return HttpResponse(menus_dto, 'application/json')


@csrf_exempt
def menu_view(request, pk):
    if request.method == 'GET':
        menu = get_menu(pk)
        menu_dto = serializers.serialize('json', menu)
        return HttpResponse(menu_dto, 'application/json')
    elif request.method == 'DELETE':
        delete_menu(pk)
        return
    elif request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        menu = body['menu']
        return update_menu(pk, menu)
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        menu = body['menu']
        return create_menu(menu)

