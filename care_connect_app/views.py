from django.shortcuts import render

def index(request):
    # retrieve info for the home page
    return render(request, 'index.html')

def search_patients(request):
    return render(request, 'search_patients.html')

def patient_programs(request):
    return render(request, 'patient_programs.html')

def patient_information(request):
    return render(request, 'patient_information.html')