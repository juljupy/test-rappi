from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import AngularApp, HorarioList, ImportHorarios


urlpatterns = [
 	url(r'^$', AngularApp.as_view(), name='home'),
 	url(r'^horarios/', HorarioList.as_view()),
 	url(r'^importhorarios/', views.horarios_upload, name="importhorarios"),
 	# url(r'^uploadhorario/', views.horarios_upload, name='horarios_upload'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

