# models.py
from django.db import models

class Tarea(models.Model):
    ESTADOS_CHOICES = (
        ('pendiente', 'pendiente'),
        ('en progreso', 'en progreso'),
        ('completada', 'completada'),
    )
    
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES)

    def __str__(self):
        return self.titulo
