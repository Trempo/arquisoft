from django.db import models

from orders.models import Order

class OrderStatus(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.description)