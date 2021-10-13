from django.db import models

from order.models import Order

class PaymentMethod(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    accountnumber = models.BigIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    cvc = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)
