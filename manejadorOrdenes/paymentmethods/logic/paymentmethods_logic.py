from django.contrib.auth.models import User, Group

from orders.models import Order
from ..models import PaymentMethod


def get_paymentmethods(user):
    paymentmethods = PaymentMethod.objects.filter(username=user)
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


def verify_paymentmethod(paymentmethod_pk, user):
    saveduser = User.objects.get(username=user)
    if saveduser.groups.all().filter(name='vendedor').exists():
        return False
    paymentmethod = PaymentMethod.objects.get(pk=paymentmethod_pk)
    if str(paymentmethod.username) == str(user):
        return True
    else:
        return False

def create_paymentmethod(new_paymentmethod, user):
    order = Order.objects.get(pk = new_paymentmethod['order'])
    paymentmethod = PaymentMethod(name=new_paymentmethod['name'], accountnumber=new_paymentmethod['accountnumber'],date=new_paymentmethod['date'],cvc=new_paymentmethod['cvc'],order=order, username=user)
    paymentmethod.save()
    return paymentmethod
