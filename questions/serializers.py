from rest_framework import serializers
from .models import Question, Exam, ExamPendingSubmit

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class ExamPendingSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamPendingSubmit
        fields = "__all__"

