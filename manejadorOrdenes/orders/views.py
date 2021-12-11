import json

import django.http
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .logic.orders_logic import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .serializers import OrderSerializer, OrderIdSerializer

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class order_view(APIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: django.http.HttpRequest):
        orders = get_orders()
        order_dto = serializers.serialize('json', orders)
        return Response(json.loads(order_dto))

    def post(self, request: django.http.HttpRequest):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        order = body['order']
        create_order(order)
        return HttpResponseRedirect('/orders/')


class order_detail_view(APIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: django.http.HttpRequest, order_pk):
        order = get_order(order_pk)
        order_dto = serializers.serialize('json', order)
        return Response(order_dto)

    def post(self, request: django.http.HttpRequest, order_pk):
        delete_order(order_pk)
        return Response('/orders/')

    def put(self, request: django.http.HttpRequest, order_pk):
        print(request.body)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        order = body['order']
        update_order(order_pk, order)
        return HttpResponseRedirect('/orders/' + str(order_pk) + '/')
