from orders.models import Order
from ..models import OrderStatus


def get_orderstatuses(order_pk):
    orderstatuses = OrderStatus.objects.filter(order=order_pk)
    return orderstatuses


def get_orderstatus(orderstatus_pk):
    orderstatus = OrderStatus.objects.filter(pk=orderstatus_pk)
    return orderstatus


def update_orderstatus(orderstatus_pk, new_orderstatus):
    order = Order.objects.get(pk=new_orderstatus['order'])
    orderstatus = OrderStatus.objects.get(pk=orderstatus_pk)
    orderstatus.description = new_orderstatus['description']
    orderstatus.order = order
    orderstatus.save()
    return orderstatus


def delete_orderstatus(orderstatus_pk):
    orderstatus = OrderStatus.objects.get(pk=orderstatus_pk)
    orderstatus.delete()


def create_orderstatus(new_orderstatus):
    order = Order.objects.get(pk = new_orderstatus['order'])
    orderstatus = OrderStatus(description=new_orderstatus['description'], order=order)
    orderstatus.save()
    return orderstatus

