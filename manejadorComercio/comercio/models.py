from django.db import models

from menu.models import Menu

class Comercio(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)
