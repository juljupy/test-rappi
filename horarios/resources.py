from import_export import resources
from .models import Horario

class HorarioResource(resources.ModelResource):
    class Meta:
        model = Horario