from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Manufacturers(models.Model):
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14)
    fax = models.CharField(max_length=14)
    website = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Diseases(models.Model):
    name = models.CharField(max_length=155)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Drug(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturers,on_delete=models.CASCADE)
    disease = models.ForeignKey(Diseases, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Generics(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturers, on_delete=models.CASCADE)
    disease = models.ForeignKey(Diseases, on_delete=models.CASCADE)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProgForms(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Program(models.Model):
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    singinc = models.IntegerField()
    coupinc = models.IntegerField()
    otherinc = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    form = models.ForeignKey(ProgForms, on_delete=models.CASCADE, blank=True)
    disease = models.ForeignKey(Diseases, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    dob = models.DateField()
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)
    ssn = models.CharField(max_length=11)
    status = models.CharField(max_length=255, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PatientInfo(models.Model):
    patient = models.ForeignKey(Patient, related_name='info', on_delete=models.CASCADE)
    insurance = models.CharField(max_length=200)
    gender = models.CharField(max_length=6)
    resident = models.BooleanField()
    veteran = models.BooleanField()
    disabled = models.BooleanField()
    allergies = models.CharField(max_length=255, blank=True)
    yearly_income = models.IntegerField()
    household_income = models.IntegerField()
    health_conditions = models.CharField(max_length=255)
    diseases = models.ForeignKey(Diseases,on_delete=models.CASCADE)
    drug = models.ForeignKey(Drug,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Insurance(models.Model):
    patient = models.ForeignKey(
        Patient, related_name="patient_coverage", on_delete=models.CASCADE)
    prescription_coverage = models.BooleanField()
    coverage_type = models.CharField(max_length=100)
    coverage_other = models.CharField(max_length=255)
    primary_name = models.CharField(max_length=100, blank=True)
    primary_phone = models.CharField(max_length=100, blank=True)
    primary_id = models.CharField(max_length=100, blank=True)
    primary_group = models.CharField(max_length=100, blank=True)
    primary_bin = models.CharField(max_length=100, blank=True)
    relation = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
