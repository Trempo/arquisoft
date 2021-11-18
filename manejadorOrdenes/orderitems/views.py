import json
from django.core import serializers
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from orderitems.logic.orderitems_logic import *
from orderitems.serializers import OrderItemSerializer


class orderitem_view(APIView):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(request, order_pk):
        orderitems = get_orderitems(order_pk)
        orderitems_dto = serializers.serialize('json', orderitems)
        return Response(json.loads(orderitems_dto))

    def post(request, order_pk):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        orderitem = body['orderitem']
        create_orderitem(orderitem)
        return HttpResponseRedirect('/orders/' + str(order_pk) + '/')


class orderitem_detail_view(APIView):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(request, order_pk, orderitem_pk):
        orderitem = get_orderitem(orderitem_pk)
        orderitem_dto = serializers.serialize('json', orderitem)
        return Response(orderitem_dto)

    def post(request, order_pk, orderitem_pk):
        delete_orderitem(orderitem_pk)
        return HttpResponseRedirect( '/orders/' + str(order_pk) + '/orderitems/')

    def put(request, order_pk, orderitem_pk):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        orderitem = body['orderitem']
        update_orderitem(orderitem_pk, orderitem)
        return HttpResponseRedirect('/orders/' + str(order_pk) + '/orderitems/' + str(orderitem_pk))
