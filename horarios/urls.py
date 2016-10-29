from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import AngularApp, HorarioList, CSVFileView


urlpatterns = [
 	url(r'^$', AngularApp.as_view(), name='home'),
 	url(r'^horarios/', HorarioList.as_view()),
 	url(r'^upload/', CSVFileView.as_view(), name='csv_file_upload'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

