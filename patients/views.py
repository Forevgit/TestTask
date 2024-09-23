from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Patient
from .serializers import PatientSerializer
from .filters import PatientFilter
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date
from .exceptions import InvalidPatientDateOfBirthEx, PermissionDeniedEx

class PatientView:
    """Basic class for Patient"""

    def valid_date_of_birth(self, serializer):
        date_of_birth = serializer.validated_data.get('date_of_birth')

        if date_of_birth > date.today():
            raise InvalidPatientDateOfBirthEx()


    def check_doctor_permission(self, patient, request):
        if patient.doctor != self.request.user:
            raise PermissionDeniedEx()

class PatientListCreateView(PatientView, generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PatientFilter

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Patient.objects.none()
        return Patient.objects.filter(doctor=self.request.user)

    def perform_create(self, serializer):
        self.valid_date_of_birth(serializer)
        serializer.save(doctor=self.request.user)

class PatientRetrieveUpdateDestroyView(PatientView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Patient.objects.none()
        return Patient.objects.filter(doctor=self.request.user)

    def perform_update(self, serializer):
        patient = self.get_object()
        self.check_doctor_permission(patient, self.request)
        self.valid_date_of_birth(serializer.validated_data['date_of_birth'])
        serializer.save()

    def perform_destroy(self, instance):
        self.check_doctor_permission(instance, self.request)
        instance.delete()
