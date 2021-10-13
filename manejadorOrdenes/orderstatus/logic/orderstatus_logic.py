from ..models import OrderStatus


def get_orderstatuses():
    orderstatuses = OrderStatus.objects.all()
    return orderstatuses


def get_orderstatus(orderstatus_pk):
    orderstatus = OrderStatus.objects.get(pk=orderstatus_pk)
    return orderstatus


def update_orderstatus(orderstatus_pk, new_orderstatus):
    orderstatus = OrderStatus.objects.get(pk=orderstatus_pk)
    orderstatus.description = new_orderstatus.description
    orderstatus.order = new_orderstatus.order
    orderstatus.save()
    return orderstatus


def delete_orderstatus(orderstatus_pk):
    orderstatus = OrderStatus.objects.get(pk=orderstatus_pk)
    orderstatus.delete()


def create_orderstatus(new_orderstatus):
    orderstatus = OrderStatus(new_orderstatus)
    orderstatus.save()
    return orderstatus
