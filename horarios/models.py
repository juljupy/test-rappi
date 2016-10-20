from django.db import models

class Horario(models.Model):
	entrada = models.DateTimeField()
	salida = models.DateTimeField()
	user_id = models.IntegerField()