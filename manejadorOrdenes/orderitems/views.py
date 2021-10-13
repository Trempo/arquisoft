import json
from django.core import serializers
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from orderitems.logic.orderitems_logic import *

@csrf_exempt
def get_orderitems_list(request, order_pk):
    if request.method == 'GET':
        orderitems = get_orderitems(order_pk)
        orderitems_dto = serializers.serialize('json', orderitems)
        return HttpResponse(orderitems_dto, 'application/json')
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        orderitem = body['orderitem']
        create_orderitem(orderitem)
        return HttpResponseRedirect('/orders/' + str(order_pk) + '/')


@csrf_exempt
def orderitem_view(request, order_pk, orderitem_pk):
    if request.method == 'GET':
        orderitem = get_orderitem(orderitem_pk)
        orderitem_dto = serializers.serialize('json', orderitem)
        return HttpResponse(orderitem_dto, 'application/json')
    elif request.method == 'DELETE':
        delete_orderitem(orderitem_pk)
        return HttpResponseRedirect( '/orders/' + str(order_pk) + '/orderitems/')
    elif request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        orderitem = body['orderitem']
        update_orderitem(orderitem_pk, orderitem)
        return HttpResponseRedirect('/orders/' + str(order_pk) + '/orderitems/' + str(orderitem_pk))
