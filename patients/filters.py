import django_filters
from .models import Patient

class PatientFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(field_name='full_name', lookup_expr='icontains')
    gender = django_filters.CharFilter(field_name='gender')
    date_of_birth = django_filters.DateFromToRangeFilter(field_name='date_of_birth')

    class Meta:
        model = Patient
        fields = ['full_name', 'gender', 'date_of_birth']
