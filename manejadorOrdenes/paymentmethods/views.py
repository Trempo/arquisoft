from django.core.serializers import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .logic.paymentmethods_logic import *
from django.http import HttpResponse
from django.core import serializers


def get_paymentmethods_list(request):
    if request.method == 'GET':
        paymentmethods = get_paymentmethods()
        paymentmethods_dto = serializers.serialize('json', paymentmethods)
        return HttpResponse(paymentmethods_dto, 'application/json')


@csrf_exempt
def paymentmethod_view(request, pk):
    if request.method == 'GET':
        paymentmethod = get_paymentmethod(pk)
        paymentmethod_dto = serializers.serialize('json', paymentmethod)
        return HttpResponse(paymentmethod_dto, 'application/json')
    elif request.method == 'DELETE':
        delete_paymentmethod(pk)
        return
    elif request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        paymentmethod = body['paymentmethod']
        return update_paymentmethod(pk, paymentmethod)
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        paymentmethod = body['paymentmethod']
        return create_paymentmethod(paymentmethod)
