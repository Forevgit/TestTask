from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Assessment
from .serializers import AssessmentSerializer
from .filters import AssessmentFilter
from .exceptions import InvalidScoreEx
from rest_framework.filters import OrderingFilter


class AssessmentView:
    """Basic class for Assessment"""

    def validate_score(self, serializer):
        score = serializer.validated_data.get('final_score')
        if score is not None and score < 0:
            raise InvalidScoreEx()

    def get_assessment_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Assessment.objects.none()
        return Assessment.objects.filter(patient__doctor=self.request.user)

class AssessmentListCreateView(AssessmentView, generics.ListCreateAPIView):
    serializer_class = AssessmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = AssessmentFilter
    ordering_fields = ['final_score', 'assessment_date']

    def get_queryset(self):
        return self.get_assessment_queryset()

    def perform_create(self, serializer):
        self.validate_score(serializer)
        serializer.save()

class AssessmentRetrieveUpdateDestroyView(AssessmentView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssessmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.get_assessment_queryset()

    def perform_create(self, serializer):
        self.validate_score(serializer)
        serializer.save()

    def perform_update(self, serializer):
        self.validate_score(serializer)
        serializer.save()
