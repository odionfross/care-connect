from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'manufacturers' : Manufacturers.objects.all(),
        'drugs' : Drug.objects.all()
    }
    return render(request, 'index.html', context)

def inputpatient(request):
    if request.method == 'POST':
        new_address = Address.objects.create(street=request.POST['street'], city=request.POST['city'], state=request.POST['state'], zipcode=request.POST['zipcode'])
        new_patient = Patient.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], address = new_address, dob=request.POST['dob'],phone=request.POST['phone'],ssn=request.POST['ssn'])
        context = {
        'patients' : Patient.objects.all()
    }
    return render(request, 'inputpatient.html', context)

def inputmanu(request):
    if request.method == 'POST':
        new_address = Address.objects.create(street=request.POST['street'], city=request.POST['city'], state=request.POST['state'], zipcode=request.POST['zipcode'])
        new_manufacturer = Manufacturers.objects.create(name=request.POST['name'],address = new_address, phone=request.POST['phone'],fax=request.POST['fax'],website=request.POST['website'])
        context = {
        'manufacturers' : Manufacturers.objects.all()
    }
    return render(request, 'inputManufacturer.html', context)

def inputdrugs(request):
    if request.method == 'POST':
        new_drug = Drug.objects.create(name=request.POST['name'])
    return redirect('/')

def inputgeneric(request):
    if request.method == 'POST':
        new_generic = Generics.objects.create(name=request.POST['name'])
        m1 = Manufacturers.objects.get(id=(request.session['manufacturer']))
    return redirect('/')