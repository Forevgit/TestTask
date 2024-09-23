from django.urls import path
from .views import AssessmentListCreateView, AssessmentRetrieveUpdateDestroyView

urlpatterns = [
    path('assessments/', AssessmentListCreateView.as_view(), name='assessment-list-create'),
    path('assessments/<int:pk>/', AssessmentRetrieveUpdateDestroyView.as_view(), name='assessment-detail'),
]
