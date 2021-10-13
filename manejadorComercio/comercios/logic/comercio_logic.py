from ..models import Comercio


def get_comercios():
    comercios = Comercio.objects.all()
    return comercios


def get_comercio(comercio_pk):
    comercio = Comercio.objects.filter(pk=comercio_pk)
    return comercio


def update_comercio(comercio_pk, new_comercio):
    comercio = Comercio.objects.get(pk=comercio_pk)
    comercio.name = new_comercio['name']
    comercio.save()
    return comercio


def delete_comercio(comercio_pk):
    comercio = Comercio.objects.get(pk=comercio_pk)
    comercio.delete()


def create_comercio(new_comercio):
    comercio = Comercio(name=new_comercio['name'])
    comercio.save()
    return comercio


