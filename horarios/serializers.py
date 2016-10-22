from rest_framework import serializers
from .models import Horario

class HorarioSerializer(serializers.ModelSerializer):
	start = serializers.SerializerMethodField('get_entrada')
	end = serializers.SerializerMethodField('get_salida')

	def get_entrada(self, obj):
		return obj.entrada

	def get_salida(self, obj):
		return obj.salida

	class Meta:
		model = Horario
		fields = ('id','start','end')
