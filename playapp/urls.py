from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path("", views.home, name="home"),
    path('student/login/', views.student_login, name="student_login"),
    path('student/register/', views.student_register, name="student_register"),
    path("student/forgot-password/", views.forgot_password, name="forgot-password"),
    path("student/reset-password/", views.reset_password, name="reset-password"),

    
]

