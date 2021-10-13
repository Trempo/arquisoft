from django.db import models

from comercio.models import Comercio

class Menu(models.Model):
    comercio = models.OneToOneField(Comercio, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)
