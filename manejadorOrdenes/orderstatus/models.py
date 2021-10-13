from django.db import models

from order.models import Order

class OrderStatus(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
    description = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.description)