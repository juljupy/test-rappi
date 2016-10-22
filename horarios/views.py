from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View
from django.template import Context

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Horario
from .serializers import HorarioSerializer

from django.http import HttpResponse
from .resources import HorarioResource

from tablib import Dataset

@method_decorator(login_required, name='dispatch')
class AngularApp(TemplateView):
  template_name = 'home.html'

  def render_to_response(self, context, **response_kwargs):
        return render(self.request, self.template_name, context)

  def get_context_data(self, **kwargs):
  	context = super(AngularApp, self).get_context_data(**kwargs)
  	context['user'] = self.request.user
  	context['ANGULAR_URL'] = settings.ANGULAR_URL
  	return context

class HorarioList(APIView):

  def get(self, request):
      horarios = Horario.objects.filter(user_id=request.user.id)
      serializer = HorarioSerializer(horarios, many=True)
      return Response(serializer.data)

class ImportHorarios(TemplateView):
  template_name = 'import.html'
  def get(self, request, *args, **kwargs):
    return render(request, self.template_name)


def horarios_upload(request):

    if request.method == 'POST':
        horario_resourse = HorarioResource()
        dataset = Dataset()
        new_horarios = request.FILES['myfile']
        print(new_horarios)

        imported_data = dataset.load(new_horarios.read())
        result = horario_resourse.import_data(dataset, dry_run=True)

        if not result.has_errors():
          horario_resourse.import_data(dataset, dry_run=False)
    
    return render(request, 'import.html')


























