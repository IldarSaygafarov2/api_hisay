from django.urls import path

from . import views


urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('categories/<str:category_id>/', views.get_requests_by_category),
    path('questions-answers/', views.QuestionAnswerList.as_view()),
    path('mainpage/images/', views.ImageItemList.as_view()),
    path('requests/', views.UserRequestCreateListView.as_view()),
    path('requests/update/<str:pk>/', views.UserRequestRetrieveUpdateAPIView.as_view()),
    path('requests/delete/<str:pk>/', views.UserRequestDeleteView.as_view()),
]
