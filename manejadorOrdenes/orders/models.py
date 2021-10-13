from django.db import models


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    cost = models.IntegerField()
    specifications = models.CharField(max_length=50)
    authorizedPerson = models.CharField(max_length=50)
    review = models.IntegerField()

    def __str__(self):
        return 'Fecha: ' + self.date + '\nPrecio: ' + self.cost + '\nEspecificaciones: ' + self.specifications \
               + '\nRecogedor autorizado: ' + self.authorizedPerson + '\nCalificacion: ' + self.review