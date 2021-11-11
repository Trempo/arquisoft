import json

import django.http
from django.contrib.auth.decorators import login_required
from .logic.orders_logic import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(['GET', 'POST'])
def list_order_view(request: django.http.HttpRequest):
    if request.method == 'GET':
        orders = get_orders()
        order_dto = serializers.serialize('json', orders)
        return HttpResponse(order_dto, 'application/json')
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        order = body['order']
        create_order(order)
        return HttpResponseRedirect('/ordenes/orders/')


def order_view(request: django.http.HttpRequest, order_pk):
    if request.method == 'GET':
        order = get_order(order_pk)
        order_dto = serializers.serialize('json', order)
        return HttpResponse(order_dto, 'application/json')
    elif request.method == 'DELETE':
        delete_order(order_pk)
        return HttpResponseRedirect('/orders/')
    elif request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        order = body['order']
        update_order(order_pk, order)
        return HttpResponseRedirect('/ordenes/orders/' + str(order_pk) + '/')
