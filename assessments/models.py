from django.db import models
from patients.models import Patient

# Create your models here.

class Assessment(models.Model):
    assessment_type = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='assessments_for_patient')
    assessment_date = models.DateField()
    final_score = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.assessment_type} for {self.patient.full_name} on {self.assessment_date}"


class Question(models.Model):
    assessment = models.ForeignKey(Assessment, related_name='assessment_questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    answer_text = models.TextField()

    def __str__(self):
        return f"Question: {self.question_text} | Answer: {self.answer_text}"
