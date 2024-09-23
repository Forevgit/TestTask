from rest_framework import serializers
from .models import Assessment, Question
from patients.models import Patient


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'answer_text']

class AssessmentSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, source='assessment_questions')
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    class Meta:
        model = Assessment
        fields = ['id', 'assessment_type', 'patient', 'assessment_date', 'questions', 'final_score']

    def create(self, validated_data):
        questions_data = validated_data.pop('assessment_questions')

        assessment = Assessment.objects.create(**validated_data)

        for question_data in questions_data:
            Question.objects.create(assessment=assessment, **question_data)

        return assessment

    def update(self, instance, validated_data):
        questions_data = validated_data.pop('assessment_questions', None)

        instance.assessment_type = validated_data.get('assessment_type', instance.assessment_type)
        instance.patient = validated_data.get('patient', instance.patient)
        instance.assessment_date = validated_data.get('assessment_date', instance.assessment_date)
        instance.final_score = validated_data.get('final_score', instance.final_score)
        instance.save()

        if questions_data:
            for question_data in questions_data:
                question_id = question_data.get('id')
                if question_id:
                    question = Question.objects.get(id=question_id, assessment=instance)
                    question.question_text = question_data.get('question_text', question.question_text)
                    question.answer_text = question_data.get('answer_text', question.answer_text)
                    question.save()
                else:
                    Question.objects.create(assessment=instance, **question_data)

        return instance

