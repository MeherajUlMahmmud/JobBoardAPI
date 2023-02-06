from django.urls import path

from .views import *

urlpatterns = [
    path('exam', ExamAPIView.as_view()),
    path('question', QuestionAPIView.as_view()),
    path('question-option', OptionAPIView.as_view()),
    path('applicant-response', ApplicantResponseAPIView.as_view()),
]
