from django.db import models

from comercios.models import Comercio


class Menu(models.Model):
    comercio = models.ForeignKey(Comercio, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)
