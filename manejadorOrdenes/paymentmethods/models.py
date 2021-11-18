from django.db import models

from orders.models import Order

class PaymentMethod(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, default="")
    accountnumber = models.BigIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    cvc = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)
