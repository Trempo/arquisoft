from ..models import PaymentMethod


def get_paymentmethods():
    paymentmethods = PaymentMethod.objects.all()
    return paymentmethods


def get_paymentmethod(paymentmethod_pk):
    paymentmethod = PaymentMethod.objects.get(pk=paymentmethod_pk)
    return paymentmethod


def update_paymentmethod(paymentmethod_pk, new_paymentmethod):
    paymentmethod = PaymentMethod.objects.get(pk=paymentmethod_pk)
    paymentmethod.name = new_paymentmethod.name
    paymentmethod.order = new_paymentmethod.order
    paymentmethod.accountnumber = new_paymentmethod.accountnumber
    paymentmethod.date = new_paymentmethod.date
    paymentmethod.cvc = new_paymentmethod.cvc
    paymentmethod.save()
    return paymentmethod


def delete_paymentmethod(paymentmethod_pk):
    paymentmethod = PaymentMethod.objects.get(pk=paymentmethod_pk)
    paymentmethod.delete()


def create_paymentmethod(new_paymentmethod):
    paymentmethod = PaymentMethod(new_paymentmethod)
    paymentmethod.save()
    return paymentmethod