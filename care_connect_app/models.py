from django.db import models

# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # address = models.ForeignKey(Address, on_delete=models.CASCADE)
    dob = models.DateField()
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)
    ssn = models.CharField(max_length=11)
    drug_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PatientInfo(models.Model):
    patient_info = models.ForeignKey(Patient, related_name='additional_info', on_delete=models.CASCADE)
    insurance = models.CharField(max_length=200)
    gender = models.CharField(max_length=6)
    resident = models.BooleanField()
    veteran = models.BooleanField()
    disabled = models.BooleanField()
    allergies = models.CharField(max_length=255, blank=True)
    yearly_income = models.IntegerField()
    household_income = models.IntegerField()
    health_conditions = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Insurance(models.Model):
    insurance = models.ForeignKey(Patient, related_name="patient_coverage", on_delete=models.CASCADE)
    prescription_coverage = models.BooleanField()
    coverage_type = models.CharField(max_length=100)
    coverage_other = models.CharField(max_length=255)
    primary_name = models.CharField(max_length=100, blank=True)
    primary_phone = models.CharField(max_length=100, blank=True)
    primary_id = models.CharField(max_length=100, blank=True)
    primary_group = models.CharField(max_length=100, blank=True)
    primary_bin = models.CharField(max_length=100, blank=True)
    secondary_name = models.CharField(max_length=100, blank=True)
    secondary_phone = models.CharField(max_length=100, blank=True)
    secondary_id = models.CharField(max_length=100, blank=True)
    secondary_group = models.CharField(max_length=100, blank=True)
    secondary_bin = models.CharField(max_length=100, blank=True)
    relation = models.CharField(max_length=100)
    relation_other = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)