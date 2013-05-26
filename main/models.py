from django.db import models
from django.contrib.auth.models import User

class Noticia(models.Model):
    titulo = models.CharField(max_length=50,unique=True)
    contenido = models.CharField(max_length = 100,null=True)
    fecha = models.DateField()

