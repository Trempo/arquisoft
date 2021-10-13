from django.db import models

from orderstatus.models import OrderStatus
from paymentmethod.models import PaymentMethod

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    cost = models.DecimalField()
    specifications = models.CharField(max_length=50)
    authorizedPerson = models.CharField(max_length=50)
    review = models.IntegerField()

    def __str__(self):
        return 'Fecha: ' + self.date + '\nPrecio: ' + self.cost + '\nEspecificaciones: ' + self.specifications \
               + '\nRecogedor autorizado: ' + self.authorizedPerson + '\nCalificacion: ' + self.review