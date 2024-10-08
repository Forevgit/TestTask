from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Patient
from .serializers import PatientSerializer
from .filters import PatientFilter
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date
from .exceptions import InvalidPatientDateOfBirthEx, PermissionDeniedEx
from rest_framework.filters import OrderingFilter

class PatientView:
    """Basic class for Patient"""

    def valid_date_of_birth(self, serializer):
        date_of_birth = serializer.validated_data.get('date_of_birth')
        if date_of_birth:
            if date_of_birth > date.today():
                raise InvalidPatientDateOfBirthEx()


    def check_doctor_permission(self, patient, request):
        if patient.doctor != self.request.user:
            raise PermissionDeniedEx()

    def get_patient_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Patient.objects.none()
        return Patient.objects.filter(doctor=self.request.user)

class PatientListCreateView(PatientView, generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = PatientFilter
    ordering_fields = ['full_name', 'date_of_birth']

    def get_queryset(self):
        return self.get_patient_queryset()

    def perform_create(self, serializer):
        self.valid_date_of_birth(serializer)
        serializer.save(doctor=self.request.user)

class PatientRetrieveUpdateDestroyView(PatientView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.get_patient_queryset()

    def perform_update(self, serializer):
        patient = self.get_object()
        self.check_doctor_permission(patient, self.request)
        self.valid_date_of_birth(serializer)
        serializer.save()

    def perform_destroy(self, instance):
        self.check_doctor_permission(instance, self.request)
        instance.delete()
