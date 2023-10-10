from django.urls import path

from . import views


urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('questions-answers/', views.QuestionAnswerList.as_view()),
    path('mainpage/images/', views.ImageItemList.as_view()),
]
