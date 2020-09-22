from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state= models.CharField(max_length=2)
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
    manufacturer = models.ManyToManyField(Manufacturers)
    disease = models.ManyToManyField(Diseases)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Generics(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ManyToManyField(Manufacturers)
    disease = models.ManyToManyField(Diseases)
    drug = models.ManyToManyField(Drug)
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
    disease = models.ManyToManyField(Diseases)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
