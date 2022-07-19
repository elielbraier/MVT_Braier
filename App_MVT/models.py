from django.db import models

class Familia(models.Model):
    
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()