from django.shortcuts import render
from .models import Exam, Question, ExamPendingSubmit
from rest_framework import generics, permissions, views
from .serializers import ExamSerializer, QuestionSerializer, ExamPendingSubmitSerializer
from rest_framework.response import Response

# Create your views here.

class ExamListCreate(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuestionListCreate(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExamPendingSubmitListCreate(generics.ListCreateAPIView):
    queryset = ExamPendingSubmit.objects.all()
    serializer_class = ExamPendingSubmitSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExamPendingSubmitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamPendingSubmit.objects.all()
    serializer_class = ExamPendingSubmitSerializer
    permission_classes = [permissions.IsAuthenticated]

class GetPendingSubmit(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response({"status": "Success"})

class AddPendingSubmit(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        return Response({"status": "Success"})