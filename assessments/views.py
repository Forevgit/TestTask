from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Assessment
from .serializers import AssessmentSerializer
from .filters import AssessmentFilter
from .exceptions import InvalidScoreEx


class AssessmentView:
    """Basic class for Assessment"""

    def validate_score(self, serializer):
        score = serializer.validated_data.get('final_score')
        if score is not None and score < 0:
            raise InvalidScoreEx()


class AssessmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AssessmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AssessmentFilter

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Assessment.objects.none()
        return Assessment.objects.filter(patient__doctor=self.request.user)

    def perform_create(self, serializer):
        self.validate_score(serializer)
        serializer.save()

class AssessmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssessmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Assessment.objects.none()
        return Assessment.objects.filter(patient__doctor=self.request.user)

    def perform_create(self, serializer):
        self.validate_score(serializer)
        serializer.save()
