from ..models import Order


def get_orders():
    orders = Order.objects.all()
    return orders


def get_order(order_pk):
    order = Order.objects.filter(pk=order_pk)
    return order


def update_order(order_pk, new_order):
    order = Order.objects.get(pk=order_pk)
    order.date = new_order.date
    order.cost = new_order.cost
    order.specifications = new_order.specifications
    order.authorizedPerson = new_order.authorizedPerson
    order.review = new_order.review
    order.save()
    return order


def delete_order(order_pk):
    order = Order.objects.get(pk=order_pk)
    order.delete()


def create_order(new_order):

    order = Order(date=new_order['date'],cost=new_order['cost'],specifications=new_order['specifications'],authorizedPerson=new_order['authorizedPerson'],review=new_order['review'])
    order.save()
    return order


