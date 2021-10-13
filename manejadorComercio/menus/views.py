import json
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .logic.menu_logic import *
from django.http import HttpResponse
from django.core import serializers


@csrf_exempt
def get_menus_list(request, comercio_pk):
    if request.method == 'GET':
        menus = get_menus(comercio_pk)
        menus_dto = serializers.serialize('json', menus)
        return HttpResponse(menus_dto, 'application/json')
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        menu = body['menu']
        create_menu(menu)
        return HttpResponseRedirect('/comercios/' + str(comercio_pk) + '/menus/')


@csrf_exempt
def menu_view(request, menu_pk, comercio_pk):
    if request.method == 'GET':
        menu = get_menu(menu_pk)
        menu_dto = serializers.serialize('json', menu)
        return HttpResponse(menu_dto, 'application/json')
    elif request.method == 'DELETE':
        delete_menu(menu_pk)
        return HttpResponseRedirect('/comercios/' + str(comercio_pk) + '/menus/')
    elif request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        menu = body['menu']
        update_menu(menu_pk, menu)
        return HttpResponseRedirect('/comercios/' + str(comercio_pk) + '/menus/' + str(menu_pk) + '/')


