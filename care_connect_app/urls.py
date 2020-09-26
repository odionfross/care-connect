from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('search_patients', views.search_patients),
	path('patient_programs', views.patient_programs),
	path('patient_information', views.patient_information)
]