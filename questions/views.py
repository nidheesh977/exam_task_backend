from django.shortcuts import render
from .models import Exam, Question, ExamPendingSubmit, Result
from rest_framework import generics, permissions, views
from .serializers import ExamSerializer, QuestionSerializer, ExamPendingSubmitSerializer, ResultSerializer
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
        user = request.user
        if ExamPendingSubmit.objects.filter(user = user).exists():
            pendingExam = ExamPendingSubmit.objects.get(user = user)
            exam = pendingExam.exam
            questions = Question.objects.filter(exam = exam)
            serializer = QuestionSerializer(questions, many = True)
            return Response(serializer.data)
        else:
            return Response({"message": "No pending exams"}, 400)

class StartExam(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        data = {"user": request.user.id, "exam": kwargs["pk"]}
        serializer = ExamPendingSubmitSerializer(data = data)
        if serializer.is_valid():
            ExamPendingSubmit.objects.filter(user = request.user).delete()
            serializer.save()
            exam = Exam.objects.get(id = kwargs["pk"])
            questions = Question.objects.filter(exam = exam)
            serializer = QuestionSerializer(questions, many = True)
            print(questions)
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response({"message": "Bad request"}, 400)

class SubmitAnswers(views.APIView):
    def post(self, request):
        try:
            user = request.user
            answers = request.data
            for i in answers:
                correct_ans = 0
                question = Question.objects.get(id = i["id"])
                question.total_submissions+=1
                if question.answer == i["answer"]:
                    correct_ans+=1
                    question.total_correct_answers+=1
                question.save()
            percentage = (correct_ans/len(answers)*100)
            exam = ExamPendingSubmit.objects.get(user = user)
            Result.objects.create(user = user, exam = exam.exam, total_correct_answers = correct_ans)
            exam.delete()
            return Response({"percentage": percentage})
        except:
            return Response({"message": "Not authorized"}, 401)

class GetResultsUser(views.APIView):
    def get(self, request):
        user = request.user
        results = Result.objects.filter(user = user)
        serializer = ResultSerializer(results, many = True)
        return Response(serializer.data)

class GetResultsAdmin(views.APIView):
    def get(self, request, *args, **kwargs):
        try:
            user = request.user
            if not Exam.objects.filter(id = kwargs["pk"]).exists():
                return Response({"message": "Invalid exam id"}, 400)
            exam = Exam.objects.get(id = kwargs["pk"])
            if user.is_superuser:
                results = Result.objects.filter(exam = exam)
                serializer = ResultSerializer(results, many = True)
                return Response(serializer.data)
            else:
                return Response({"message": "User is not admin. Login as admin"}, 401)
        except:
            return Response({"message": "User is not admin. Login as admin"}, 401)

class CheckIsSuperUser(views.APIView):
    def get(self, request):
        user = request.user
        if user.is_superuser:
            return Response({"message": "Admin"})
        return Response({"message": "User"}, 401)

class CheckIsUser(views.APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            print("Authenticated")
            return Response({"message": "Authenticated"})
        return Response({"message": "Error"}, 401)

class CreateQuestion(views.APIView):
    def post(self, request):
        questions = request.data
        for question in questions:
            serializer = QuestionSerializer(data = question)
            if serializer.is_valid():
                serializer.save()
            else:
                print("Error")
                return Response({"message": "Bad request"}, 400)
        return Response({"message": "Created successfully"})