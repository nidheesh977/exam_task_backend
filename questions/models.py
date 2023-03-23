from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Exam(models.Model):
    title = models.CharField(max_length = 200, unique = True)

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete = models.CASCADE)
    question = models.TextField()
    optionA = models.CharField(max_length = 200)
    optionB = models.CharField(max_length = 200)
    optionC = models.CharField(max_length = 200)
    optionD = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 2)

class ExamPendingSubmit(models.Model):
    exam = models.ForeignKey(Exam, on_delete = models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)