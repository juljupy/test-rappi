from django.db import models
from csvImporter.model import CsvDbModel
import os

class Horario(models.Model):
	entrada = models.DateTimeField()
	salida = models.DateTimeField()
	user_id = models.IntegerField()

class MyCsvModel(CsvDbModel):

	class Meta:
		dbModel = Horario
		delimiter = ";"