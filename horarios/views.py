from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View
from django.template import Context
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Horario, MyCsvModel
from .serializers import HorarioSerializer

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from tablib import Dataset

@method_decorator(login_required, name='dispatch')
class AngularApp(TemplateView):

  template_name = 'home.html'
  @csrf_exempt
  def get_context_data(self, **kwargs):
  	context = super(AngularApp, self).get_context_data(**kwargs)
  	context['user'] = self.request.user
  	context['ANGULAR_URL'] = settings.ANGULAR_URL
  	return context


class CSVFileView(TemplateView):

    template_name = 'home.html'

    def post(self, request, *args, **kwargs):
        handle_uploaded_file(request.FILES['file'])
        my_csv_list = MyCsvModel.import_data(data = open(settings.MEDIA_ROOT + "/hors.csv"), extra_fields=str(request.user.id))

        return HttpResponseRedirect(reverse('home'))

        # return HttpResponse("Successful")


def handle_uploaded_file(f):
    with open(settings.MEDIA_ROOT + '/hors.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

class HorarioList(APIView):

  def get(self, request):
      horarios = Horario.objects.filter(user_id=request.user.id)
      serializer = HorarioSerializer(horarios, many=True)
      return Response(serializer.data)

























