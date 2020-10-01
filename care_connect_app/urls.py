from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('inputpatient', views.inputpatient),
	path('inputmanu', views.inputmanu),
	path('inputdrugs', views.inputdrugs),
	path('inputgeneric', views.inputgeneric),
	path('inputinfo', views.inputinfo),
	path('patients', views.patients),
	path('programs', views.programs),
	path('disease', views.diseaseinput),
	path('patinfo/<int:patient_id>', views.patinfo),
	path('inputpatient', views.inputpatient),
]