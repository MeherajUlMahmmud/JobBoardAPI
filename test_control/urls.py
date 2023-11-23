from django.urls import path

from test_control.views.exam import (
    GetExamListAPIView, CreateExamAPIView, GetExamDetailsAPIView, UpdateExamAPIView,
)
from test_control.views.option import (
    GetOptionListAPIView, CreateOptionAPIView, GetOptionDetailsAPIView, UpdateOptionDetailsAPIView, DeleteOptionAPIView,
)
from test_control.views.question import (
    GetQuestionListAPIView, CreateQuestionAPIView, GetQuestionListByExamAPIView, GetQuestionDetailsAPIView, UpdateQuestionAPIView,
)


urlpatterns = [
    # Exam URLs
    path('exam/', GetExamListAPIView.as_view()),
    path('exam/create/', CreateExamAPIView.as_view()),
    path('exam/<str:pk>/details/', GetExamDetailsAPIView.as_view()),
    path('exam/<str:pk>/update/', UpdateExamAPIView.as_view()),

    # Question URLs
    path('question/', GetQuestionListAPIView.as_view()),
    path('question/create/', CreateQuestionAPIView.as_view()),
    path('question/<str:exam_id>/', GetQuestionListByExamAPIView.as_view()),
    path('question/<str:pk>/details/', GetQuestionDetailsAPIView.as_view()),
    path('question/<str:pk>/update/', UpdateQuestionAPIView.as_view()),

    # Option URLs
    path('option/', GetOptionListAPIView.as_view()),
    path('option/create/', CreateOptionAPIView.as_view()),
    path('option/<str:question_id>/', GetOptionListAPIView.as_view()),
    path('option/<str:pk>/details/', GetOptionDetailsAPIView.as_view()),
    path('option/<str:pk>/update/', UpdateOptionDetailsAPIView.as_view()),
    path('option/<str:pk>/delete/', DeleteOptionAPIView.as_view()),

]