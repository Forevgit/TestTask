from datetime import date

from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    doctor = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'full_name', 'gender', 'phone_number', 'date_of_birth', 'age', 'address', 'doctor']

    def get_age(self, obj):
        """Calculate age"""
        return date.today().year - obj.date_of_birth.year