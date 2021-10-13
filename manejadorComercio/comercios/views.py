import json
from django.views.decorators.csrf import csrf_exempt

from .logic.comercio_logic import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers


@csrf_exempt
def list_comercio_view(request):
    if request.method == 'GET':
        comercios = get_comercios()
        comercio_dto = serializers.serialize('json', comercios)
        return HttpResponse(comercio_dto, 'application/json')
    elif request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        comercio = body['comercio']
        create_comercio(comercio)
        return HttpResponseRedirect('/comercios/')


@csrf_exempt
def comercio_view(request, comercio_pk):
    if request.method == 'GET':
        comercio = get_comercio(comercio_pk)
        comercio_dto = serializers.serialize('json', comercio)
        return HttpResponse(comercio_dto, 'application/json')
    elif request.method == 'DELETE':
        delete_comercio(comercio_pk)
        return HttpResponseRedirect('/comercios/')
    elif request.method == 'PUT':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        comercio = body['comercio']
        update_comercio(comercio_pk, comercio)
        return HttpResponseRedirect('/comercios/' + str(comercio_pk) + '/')



