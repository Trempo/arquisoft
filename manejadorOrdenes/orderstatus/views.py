import json
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .logic.orderstatus_logic import *
from django.http import HttpResponse
from django.core import serializers


@csrf_exempt
def get_orderstatuses_list(request, order_pk):
    if request.method == 'GET':
        orderstatuses = get_orderstatuses(order_pk)
        orderstatuses_dto = serializers.serialize('json', orderstatuses)
        return HttpResponse(orderstatuses_dto, 'application/json')
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        orderstatus = body['orderstatus']
        create_orderstatus(orderstatus)
        return HttpResponseRedirect('/orders/' + str(order_pk) + '/orderstatus/')


@csrf_exempt
def orderstatus_view(request, orderstatus_pk, order_pk):
    if request.method == 'GET':
        orderstatus = get_orderstatus(orderstatus_pk)
        orderstatus_dto = serializers.serialize('json', orderstatus)
        return HttpResponse(orderstatus_dto, 'application/json')
    elif request.method == 'DELETE':
        delete_orderstatus(orderstatus_pk)
        return HttpResponseRedirect('/orders/' + str(order_pk) + '/orderstatus/')
    elif request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        orderstatus = body['orderstatus']
        update_orderstatus(orderstatus_pk, orderstatus)
        return HttpResponseRedirect('/orders/' + str(order_pk) + '/orderstatus/' + str(orderstatus_pk) + '/')


