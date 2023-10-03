from django.urls import path

from . import views

urlpatterns = [
    path('save/user/', views.save_user),
    path('save/bot/data/', views.save_data_from_bot),
    path("users/code/check/", views.check_verification_code),
]

