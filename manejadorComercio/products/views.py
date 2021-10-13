import json
from django.core import serializers
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from products.logic.product_logic import *

@csrf_exempt
def get_products_list(request, comercio_pk, menu_pk):
    if request.method == 'GET':
        products = get_products(menu_pk)
        products_dto = serializers.serialize('json', products)
        return HttpResponse(products_dto, 'application/json')
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        product = body['product']
        create_product(product)
        return HttpResponseRedirect('/comercios/' + str(comercio_pk) + '/menus/' + str(menu_pk) + '/')


@csrf_exempt
def product_view(request, comercio_pk, menu_pk, product_pk):
    if request.method == 'GET':
        product = get_product(product_pk)
        product_dto = serializers.serialize('json', product)
        return HttpResponse(product_dto, 'application/json')
    elif request.method == 'DELETE':
        delete_product(product_pk)
        return HttpResponseRedirect('/comercios/' + str(comercio_pk) + '/menus/' + str(menu_pk) + '/products/') 
    elif request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        product = body['product']
        update_product(product_pk, product)
        return HttpResponseRedirect('/comercios/' + str(comercio_pk) + '/menus/' + str(menu_pk) + '/products/' + str(product_pk))
