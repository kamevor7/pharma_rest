from rest_framework import serializers
from .models import Location, Patient, Prescription


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'pk',
            'store_number',
            'address',
            'phone_number',
            'city',
            'state',
            'zipcode',
        )


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            'pk',
            'patient_number',
            'first_name',
            'last_name',
            'date_of_birth',
            'address',
            'city',
            'state',
            'zipcode',
            'email',
            'cell_phone',
        )


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = (
            'pk',
            'patient',
            'patient_number',
            'rx_number',
            'name',
            'dosage',
            'description',
            'refill',
            'cost',
            'prescription_date',
            'status',
            'pickup_date',
        )
