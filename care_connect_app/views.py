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
        dis = Diseases.objects.get(id=request.POST['disease'])
        man = Manufacturers.objects.get(id=request.POST['manufacturer'])
        new_drug = Drug.objects.create(name=request.POST['name'],manufacturer = man,disease = dis)
    return redirect('/inputinfo')


def inputgeneric(request):
    if request.method == 'POST':
        dis = Diseases.objects.get(id=request.POST['disease'])
        man = Manufacturers.objects.get(id=request.POST['manufacturer'])
        relDrug = Drug.objects.get(id=request.POST['drug'])
        new_generic = Generics.objects.create(name=request.POST['name'],manufacturer = man, disease = dis, drug = relDrug)
    return redirect('/inputinfo')

def diseaseinput(request):
    if request.method == 'POST':
        new_disease = Diseases.objects.create(name=request.POST['name'])
    return redirect('/inputinfo')

def inputinfo(request):
    context = {
        'manufacturers': Manufacturers.objects.all(),
        'drugs': Drug.objects.all(),
        'patients': Patient.objects.all(),
        'generics': Generics.objects.all(),
        'diseases': Diseases.objects.all(),
        'programs': Program.objects.all(),
        'forms': ProgForms.objects.all(),
    }
    return render(request, 'inputinfo.html', context)


def patients(request):
    context = {
        'patients': Patient.objects.all(),
    }
    return render(request, 'patient.html', context)

def programs(request):
    context = {
        'programs': Program.objects.all(),
    }
    return render(request, 'programlist.html', context)

def patinfo(request, patient_id):
    context = {
        'patient' : Patient.objects.get(id=patient_id),
        'drugs': Drug.objects.all(),
        'diseases': Diseases.objects.all(),
    }
    return render(request, 'inputpatinfo.html', context)

def inputpatient(request):
    if request.method == 'POST':
        pat = Patient.objects.get(id=request.POST['patient'])
        dis = Diseases.objects.get(id=request.POST['disease'])
        relDrug = Drug.objects.get(id=request.POST['drug'])
        new_info = PatientInfo.objects.create(patient=pat, insurance = request.POST['insurance'], gender = request.POST['gender'], resident = request.POST['resident'], veteran=request.POST['veteran'], disabled=request.POST['disabled'],allergies=request.POST['allergies'],yearly_income=request.POST['yearly_income'],household_income=request.POST['household_income'],health_conditions=request.POST['healthconditions'], diseases=dis, drug=relDrug)
    return redirect('/inputinfo')

def inputprog(request):
    if request.method == 'POST':
        relatedForm = ProgForms.objects.get(id=request.POST['form'])
        relatedDisease = Diseases.objects.get(id=request.POST['disease'])
        new_address = Address.objects.create(
            street=request.POST['street'], city=request.POST['city'], state=request.POST['state'], zipcode=request.POST['zipcode'])
        new_prog = Program.objects.create(name=request.POST['name'],address=new_address,singinc=request.POST['single_income'],coupinc=request.POST['couple_income'],otherinc=request.POST['other_income'],active=request.POST['active'],form=relatedForm, disease=relatedDisease) 
    return redirect('/inputinfo')

def inputprogform(request):
    if request.method == 'POST':
        new_form = ProgForms.objects.create(name=request.POST['name'])
    return redirect('/inputinfo')

def application(request):
    return render(request, 'application.html')