from django.db import models

from order.models import Order

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return 'Nombre: ' + self.name + '\nPrecio: ' + self.price + '\nCantidad: ' + self.quantity