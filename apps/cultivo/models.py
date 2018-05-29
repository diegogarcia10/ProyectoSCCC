from django.db import models

# Create your models here.
class Categorizacion(models.Model)
    categoria = models.IntegerField()

class MineralesDelSuelo(models.Model):
    humedad = Categorizacion
    minerales = Categorizacion

class TipoSuelo(models.Model)
    tipoSuelo = models.CharField(max_lenght=50)
    isHomogeneo = models.BooleanField()
    textura = Categorizacion
    degradacion = Categorizacion
    aradoDelSuelo = Categorizacion

class Topografia(models.Model)
    topografia = models.CharField(max_length=50)
    descipcion = models.CharField(max_length=200)
    temperaturaProm = models.DecimalField()
    altitud = models.DecimalField()
    lluvias = Categorizacion
    radiacion = Categorizacion



