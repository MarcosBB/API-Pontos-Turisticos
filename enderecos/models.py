from django.db import models

class Endereco(models.Model):
    linha1 = models.CharField(max_length=150)
    linha2 = models.CharField(max_length=150)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=70)
    latitude = models.IntegerField(null=True, blank=True)
    longititude = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.linha1

    
