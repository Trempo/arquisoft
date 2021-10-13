from django.core.serializers import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .logic.orderstatus_logic import *
from django.http import HttpResponse
from django.core import serializers


def get_orderstatuses_list(request):
    if request.method == 'GET':
        orderstatuses = get_orderstatuses()
        orderstatuses_dto = serializers.serialize('json', orderstatuses)
        return HttpResponse(orderstatuses_dto, 'application/json')


@csrf_exempt
def orderstatus_view(request, pk):
    if request.method == 'GET':
        orderstatus = get_orderstatus(pk)
        orderstatus_dto = serializers.serialize('json', orderstatus)
        return HttpResponse(orderstatus_dto, 'application/json')
    elif request.method == 'DELETE':
        delete_orderstatus(pk)
        return
    elif request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        orderstatus = body['orderstatus']
        return update_orderstatus(pk, orderstatus)
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        orderstatus = body['orderstatus']
        return create_orderstatus(orderstatus)