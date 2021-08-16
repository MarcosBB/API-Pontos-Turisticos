from comentarios.models import Comentario
from django.contrib.auth.models import User
from django.db import models

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(null=True, blank=True)
    nota = models.DecimalField(decimal_places=2, max_digits=3)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username