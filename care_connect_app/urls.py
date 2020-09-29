from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('inputpatient', views.inputpatient),
	path('inputmanu', views.inputmanu),
	path('inputdrugs', views.inputdrugs),
	path('inputgeneric', views.inputgeneric),
]