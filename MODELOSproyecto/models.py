from django.db import models

class Informacion(models.model):
    items = models.CharField(max_length=75)