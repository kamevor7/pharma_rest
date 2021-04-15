from django.db import models
from django.utils import timezone


class Location(models.Model):
    store_number = models.IntegerField(blank=False, null=False)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=10)
    zipcode = models.CharField(max_length=10)

    class Meta:
        ordering = ['store_number']

    def __str__(self):
        return f'{self.store_number}, {self.city}'


class Patient(models.Model):
    patient_number = models.IntegerField(blank=False, null=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    cell_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.patient_number)


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    rx_number = models.IntegerField(blank=False, null=False)
    name = models.CharField(max_length=50)
    dosage = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    refill = models.IntegerField(blank=False, null=False)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    prescription_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=50)
    pickup_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(default=timezone.now, blank=True, null=True)

    def created(self):
        self.prescription_date = timezone.now()
        self.save()

    def updated(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.patient)

    def patient_number(self):
        return self.patient.patient_number
