from django.db import models

class Ingrediente(models.Model):
    #id = models.IntegerField()
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    #hamburguesa = models.ForeignKey(Hamburguesa, related_name='ingredientes', on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombre


class Hamburguesa(models.Model):
    #id = models.IntegerField()
    nombre = models.CharField(max_length=100, null=False, blank=False)
    precio = models.IntegerField(null=False, blank=False)
    descripcion = models.CharField(max_length=200, null=False, blank=False)
    imagen = models.CharField(max_length=300, null=False, blank=False)
    ingredientes = models.ManyToManyField(Ingrediente, blank=True)

    def __str__(self):
        return self.nombre

    
