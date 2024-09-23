import django_filters
from .models import Assessment

class AssessmentFilter(django_filters.FilterSet):
    assessment_type = django_filters.CharFilter(lookup_expr='icontains')  # case insensitive
    patient = django_filters.NumberFilter(field_name='patient__id', lookup_expr='exact')
    assessment_date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Assessment
        fields = ['assessment_type', 'patient', 'assessment_date']
