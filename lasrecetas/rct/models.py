from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  # only if you need to support Python 2
class Receta(models.Model):
  titulo = models.CharField(max_length=100, unique=True)
  ingredientes = models.TextField(help_text='Redacta los ingredientes')
  prepacion = models.TextField(verbose_name='Preparación')
  tiempo_registro = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.titulo

  def publicado_hoy(self):
    return self.tiempo_registro.date() == timezone.now().date()
  publicado_hoy.boolean = True
  publicado_hoy.prepacion = '¿Agregado hoy?'

@python_2_unicode_compatible  # only if you need to support Python 2
class Comentario(models.Model):
  Receta = models.CharField(max_length=50)
  ingredientes = models.TextField()
  preparacion = models.TextField()

  def __str__(self):
    return self.preparacion
  
