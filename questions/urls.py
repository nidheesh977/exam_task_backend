from django.urls import path 
from . import views

urlpatterns = [
    path("question/", views.QuestionListCreate.as_view()),
    path("question/<str:pk>/", views.QuestionDetailView.as_view()),
    path("exam/", views.ExamListCreate.as_view()),
    path("exam/<str:pk>/", views.ExamDetailView.as_view()),
    path("exam-pending-submit/", views.ExamPendingSubmitListCreate.as_view()),
    path("exam-pending-submit/<str:pk>/", views.ExamPendingSubmitDetailView.as_view()),
    path("get-pending-submit-exam/", views.GetPendingSubmit.as_view()),
    path("start-exam/<str:pk>/", views.StartExam.as_view()),
    path("submit-answer/", views.SubmitAnswers.as_view()),
    path("get-result-user/", views.GetResultsUser.as_view()),
    path("get-result-admin/<str:pk>/", views.GetResultsAdmin.as_view()),
    path("check-admin/", views.CheckIsSuperUser.as_view()),
    path("check-user/", views.CheckIsUser.as_view()),
    path("create-question/", views.CreateQuestion.as_view()),
]