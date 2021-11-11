import json
from django.contrib.auth.decorators import login_required
from .logic.orders_logic import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from manejadorOrdenes.auth0backend import Auth0


@login_required
def list_order_view(request):
    if request.method == 'GET':
        Auth0().getRole(request)
        orders = get_orders()
        order_dto = serializers.serialize('json', orders)
        return HttpResponse(order_dto, 'application/json')
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        order = body['order']
        create_order(order)
        return HttpResponseRedirect('/ordenes/orders/')


@login_required
def order_view(request, order_pk):
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



