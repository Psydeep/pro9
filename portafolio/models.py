from __future__ import unicode_literals

from django.db import models

# Create your models here.
class registrados(models.Model):
	nombre = models.CharField(max_length=100, blank=True, null=True) # el nombre no es obligatorio
	email =  models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) #marca de tiempo

	#devuelve correo en la consola cuando se registra 
	def __unicode__(self): #python 2 (para la version 2)
		return self.email

	def __str__(self): #python 3 (para la version 3)
		return self.email
