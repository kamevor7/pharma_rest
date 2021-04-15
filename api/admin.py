from django.contrib import admin
from .models import Location, Patient, Prescription


class PatientList(admin.ModelAdmin):
    list_display = ('patient_number', 'last_name', 'first_name', 'cell_phone')
    list_filter = ('patient_number', 'last_name', 'city')
    search_fields = ('patient_number', 'last_name', 'first_name')
    ordering = ['last_name']


class PrescriptionList(admin.ModelAdmin):
    list_display = ('patient', 'rx_number', 'name', 'cost', 'refill')
    list_filter = ('name', 'rx_number')
    search_fields = ('name', 'rx_number')
    ordering = ['patient']


class LocationList(admin.ModelAdmin):
    list_display = ('store_number', 'address', 'city', 'state', 'zipcode')
    list_filter = ('store_number', 'city',)
    search_fields = ('store_number', 'city', 'state', 'zipcode')
    ordering = ['store_number']


admin.site.register(Location, LocationList)
admin.site.register(Patient, PatientList)
admin.site.register(Prescription, PrescriptionList)
