from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Exam(models.Model):
    title = models.CharField(max_length = 200, unique = True)

    @property
    def no_of_questions(self):
        questions = self.question_set.all()
        return len(questions)

    def __str__(self):
        return self.title

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete = models.CASCADE)
    question = models.TextField()
    optionA = models.CharField(max_length = 200)
    optionB = models.CharField(max_length = 200)
    optionC = models.CharField(max_length = 200)
    optionD = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 2)
    total_submissions = models.IntegerField(default = 0)
    total_correct_answers = models.IntegerField(default = 0)

    def __str__(self):
        return self.question

class ExamPendingSubmit(models.Model):
    exam = models.ForeignKey(Exam, on_delete = models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)

class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete = models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    total_correct_answers = models.IntegerField(default = 0)
    submitted_date = models.DateField(auto_now_add = True)
    @property
    def total_questions(self):
        questions = Question.objects.filter(exam = self.exam)
        return len(questions)

    def __str__(self):
        return self.exam.title