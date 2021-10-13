from django.db import models

from menu.models import Menu

class Product(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return 'Nombre: ' + self.name + '\nPrecio: ' + self.price + '\nStock: ' + self.stock
