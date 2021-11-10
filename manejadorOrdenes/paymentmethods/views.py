import json

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from .logic.paymentmethods_logic import *
from django.http import HttpResponse
from django.core import serializers


@login_required
def get_paymentmethods_list(request, order_pk):
    if request.method == 'GET':
        paymentmethods = get_paymentmethods(order_pk)
        paymentmethods_dto = serializers.serialize('json', paymentmethods)
        return HttpResponse(paymentmethods_dto, 'application/json')
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        paymentmethod = body['paymentmethod']
        create_paymentmethod(paymentmethod)
        return HttpResponseRedirect('/orders/' + str(order_pk) + '/paymentmethods/')


@login_required
def paymentmethod_view(request, paymentmethod_pk, order_pk):
    if request.method == 'GET':
        paymentmethod = get_paymentmethod(paymentmethod_pk)
        paymentmethod_dto = serializers.serialize('json', paymentmethod)
        return HttpResponse(paymentmethod_dto, 'application/json')
    elif request.method == 'DELETE':
        delete_paymentmethod(paymentmethod_pk)
        return HttpResponseRedirect('/orders/' + str(order_pk) + '/paymentmethods/')
    elif request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        paymentmethod = body['paymentmethod']
        update_paymentmethod(paymentmethod_pk, paymentmethod)
        return HttpResponseRedirect('/orders/' + str(order_pk) + '/paymentmethods/' + str(paymentmethod_pk) + '/')



