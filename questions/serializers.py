from rest_framework import serializers
from .models import Question, Exam, ExamPendingSubmit, Result

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ["id", "title", "no_of_questions"]

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class ExamPendingSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamPendingSubmit
        fields = "__all__"

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ["exam", "user", "total_correct_answers", "total_questions", "submitted_date"]
        depth = 1

