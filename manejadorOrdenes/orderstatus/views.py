import json
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .logic.orderstatus_logic import *
from django.http import HttpResponse
from django.core import serializers

from .serializers import OrderStatusSerializer


class orderstatus_view(APIView):
    serializer_class = OrderStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(request, order_pk):
        orderstatuses = get_orderstatuses(order_pk)
        orderstatuses_dto = serializers.serialize('json', orderstatuses)
        return Response(json.loads(orderstatuses_dto))

    def post(request, order_pk):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        orderstatus = body['orderstatus']
        create_orderstatus(orderstatus)
        return HttpResponseRedirect('/orders/' + str(order_pk) + '/orderstatus/')

class orderstatus_detail_view(APIView):
    serializer_class = OrderStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(request, orderstatus_pk, order_pk):
        orderstatus = get_orderstatus(orderstatus_pk)
        orderstatus_dto = serializers.serialize('json', orderstatus)
        return Response(json.loads(orderstatus_dto))

    def post(request, orderstatus_pk, order_pk):
        delete_orderstatus(orderstatus_pk)
        return HttpResponseRedirect('/orders/' + str(order_pk) + '/orderstatus/')

    def put(request, orderstatus_pk, order_pk):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        orderstatus = body['orderstatus']
        update_orderstatus(orderstatus_pk, orderstatus)
        return HttpResponseRedirect('/orders/' + str(order_pk) + '/orderstatus/' + str(orderstatus_pk) + '/')
