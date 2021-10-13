from orders.models import Order
from orderitems.models import OrderItem


def get_orderitems(order_pk):
    orderitems = OrderItem.objects.filter(order=order_pk)
    return orderitems


def get_orderitem(orderitem_pk):
    orderitem = OrderItem.objects.filter(pk=orderitem_pk)
    return orderitem


def update_orderitem(orderitem_pk, new_orderitem):
    order = Order.objects.get(pk=new_orderitem['order'])
    orderitem = OrderItem.objects.get(pk=orderitem_pk)
    orderitem.order = order
    orderitem.name = new_orderitem['name']
    orderitem.price = new_orderitem['price']
    orderitem.quantity = new_orderitem['quantity']
    orderitem.save()
    return orderitem


def delete_orderitem(orderitem_pk):
    orderitem = OrderItem.objects.get(pk=orderitem_pk)
    orderitem.delete()


def create_orderitem(new_orderitem):
    order = Order.objects.get(pk = new_orderitem['order'])
    orderitem = OrderItem(order = order, name = new_orderitem['name'], price = new_orderitem['price'], quantity = new_orderitem['quantity'])
    orderitem.save()
    return orderitem
