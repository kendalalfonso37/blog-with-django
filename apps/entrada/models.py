from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Articulo(models.Model):
	titulo = models.CharField(max_length=200)
	fecha = models.DateTimeField()
	slug = models.SlugField()
	contenido = HTMLField()

	def __str__(self):
		return self.titulo

