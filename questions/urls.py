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
    path("add-pending-submit-exam/", views.AddPendingSubmit.as_view()),
]