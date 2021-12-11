import json

import django
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .logic.paymentmethods_logic import *
from django.http import HttpResponse
from django.core import serializers
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import PaymentMethodSerializer


class paymentmethods_view(APIView):
    serializer_class = PaymentMethodSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: django.http.HttpRequest):
        user = (JWTAuthentication().authenticate(request))[0]
        paymentmethods = get_paymentmethods(user)
        paymentmethods_dto = serializers.serialize('json', paymentmethods)
        return Response(json.loads(paymentmethods_dto))

    def post(self, request: django.http.HttpRequest):
        user = (JWTAuthentication().authenticate(request))[0]
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        paymentmethod = body['paymentmethod']
        create_paymentmethod(paymentmethod, user)
        return HttpResponseRedirect('/paymentmethods/')


class paymentmethodsdetail_view(APIView):
    serializer_class = PaymentMethodSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, paymentmethod_pk):
        user = (JWTAuthentication().authenticate(request))[0]
        if verify_paymentmethod(paymentmethod_pk, user):
            paymentmethod = get_paymentmethod(paymentmethod_pk)
            paymentmethod_dto = serializers.serialize('json', paymentmethod)
            return Response(json.loads(paymentmethod_dto))
        else:
            return HttpResponse(status=401)

    def post(self, request, paymentmethod_pk):
        user = (JWTAuthentication().authenticate(request))[0]
        if verify_paymentmethod(paymentmethod_pk, user):
            delete_paymentmethod(paymentmethod_pk)
            return HttpResponseRedirect('/paymentmethods/')
        else:
            return HttpResponse(status=401)

    def put(self, request, paymentmethod_pk):
        user = (JWTAuthentication().authenticate(request))[0]
        if (verify_paymentmethod(paymentmethod_pk, user)):
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            paymentmethod = body['paymentmethod']
            update_paymentmethod(paymentmethod_pk, paymentmethod)
            return HttpResponseRedirect('/paymentmethods/' + str(paymentmethod_pk) + '/')
        else:
            return HttpResponse(status=401)
