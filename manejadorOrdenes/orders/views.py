import json
from django.views.decorators.csrf import csrf_exempt

from .logic.orders_logic import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers


@csrf_exempt
def list_order_view(request):
    if request.method == 'GET':
        orders = get_orders()
        order_dto = serializers.serialize('json', orders)
        return HttpResponse(order_dto, 'application/json')
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        order = body['order']
        create_order(order)
        return HttpResponseRedirect('/orders/')


@csrf_exempt
def order_view(request, pk):
    if request.method == 'GET':
        order = get_order(pk)
        order_dto = serializers.serialize('json', order)
        return HttpResponse(order_dto, 'application/json')
    elif request.method == 'DELETE':
        delete_order(pk)
        return HttpResponseRedirect('/orders/')
    elif request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        order = body['order']
        update_order(pk, order)
        return HttpResponseRedirect('/orders/id/11/')



