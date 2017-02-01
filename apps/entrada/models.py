from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField

# Create your models here.
class Articulo(models.Model):
	titulo = models.CharField(max_length=200)
	fecha = models.DateTimeField()
	slug = models.SlugField(editable=False)
	contenido = HTMLField()

	def __str__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Articulo, self).save(*args, **kwargs)

