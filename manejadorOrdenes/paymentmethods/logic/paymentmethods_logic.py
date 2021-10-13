from orders.models import Order
from ..models import PaymentMethod


def get_paymentmethods(order_pk):
    paymentmethods = PaymentMethod.objects.filter(order=order_pk)
    return paymentmethods


def get_paymentmethod(paymentmethod_pk):
    paymentmethod = PaymentMethod.objects.filter(pk=paymentmethod_pk)
    return paymentmethod


def update_paymentmethod(paymentmethod_pk, new_paymentmethod):
    order = Order.objects.get(pk=new_paymentmethod['order'])
    paymentmethod = PaymentMethod.objects.get(pk=paymentmethod_pk)
    paymentmethod.name = new_paymentmethod['name']
    paymentmethod.accountnumber = new_paymentmethod['accountnumber']
    paymentmethod.date = new_paymentmethod['date']
    paymentmethod.cvc = new_paymentmethod['cvc']
    paymentmethod.order = order
    paymentmethod.save()
    return paymentmethod


def delete_paymentmethod(paymentmethod_pk):
    paymentmethod = PaymentMethod.objects.get(pk=paymentmethod_pk)
    paymentmethod.delete()


def create_paymentmethod(new_paymentmethod):
    order = Order.objects.get(pk = new_paymentmethod['order'])
    paymentmethod = PaymentMethod(name=new_paymentmethod['name'], accountnumber=new_paymentmethod['accountnumber'],date=new_paymentmethod['date'],cvc=new_paymentmethod['cvc'],order=order)
    paymentmethod.save()
    return paymentmethod
