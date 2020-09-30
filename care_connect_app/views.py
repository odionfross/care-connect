from django.shortcuts import render, redirect
from .models import *


def index(request):
    context = {
        'manufacturers': Manufacturers.objects.all(),
        'drugs': Drug.objects.all()
    }
    return render(request, 'index.html', context)


def inputpatient(request):
    if request.method == 'POST':
        new_address = Address.objects.create(
            street=request.POST['street'], city=request.POST['city'], state=request.POST['state'], zipcode=request.POST['zipcode'])
        new_patient = Patient.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
                                             email=request.POST['email'], address=new_address, dob=request.POST['dob'], phone=request.POST['phone'], ssn=request.POST['ssn'])
    return redirect('/inputinfo')


def inputmanu(request):
    if request.method == 'POST':
        new_address = Address.objects.create(
            street=request.POST['street'], city=request.POST['city'], state=request.POST['state'], zipcode=request.POST['zipcode'])
        new_manufacturer = Manufacturers.objects.create(
            name=request.POST['name'], address=new_address, phone=request.POST['phone'], fax=request.POST['fax'], website=request.POST['website'])
    return redirect('/inputinfo')


def inputdrugs(request):
    if request.method == 'POST':
        new_drug = Drug.objects.create(name=request.POST['name'])
        new_manufacturer = Manufacturers.objects.get(id=request.POST['manufacturer'])
        new_disease = Diseases.objects.get(id=(request.POST['disease']))
        new_drug.manufacturer.add(new_manufacturer)
        new_drug.disease.add(new_disease)
        new_drug.save()
    return redirect('/inputinfo')


def inputgeneric(request):
    if request.method == 'POST':
        new_generic = Generics.objects.create(name=request.POST['name'])
        m1 = Manufacturers.objects.get(id=(request.session['manufacturer']))
        new_disease = Diseases.objects.get(id=(request.POST['disease']))
        new_generic.manufacturer.add(m1)
        new_generic.disease.add(new_disease)
        new_generic.save()
    return redirect('/inputinfo')


def inputinfo(request):
    context = {
        'manufacturers': Manufacturers.objects.all(),
        'drugs': Drug.objects.all(),
        'patients': Patient.objects.all(),
        'generics': Generics.objects.all(),
        'diseases': Diseases.objects.all(),
    }
    return render(request, 'inputinfo.html', context)
