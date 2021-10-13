from django.db import models

from menus.models import Menu


class Product(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return 'Nombre: ' + self.name + '\nPrecio: ' + str(self.price) + '\nStock: ' + str(self.stock)
