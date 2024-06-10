from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/student/', views.register_student, name='register_student'),
    path('register/subject/', views.register_subject, name='register_subject'),
    path('register/grade/', views.register_grade, name='register_grade'),
    path('students/', views.student_list, name='student_list'),
    path('subjects/', views.subject_list, name='subject_list'),
    path('grades/', views.grade_list, name='grade_list'),
    path('students/report/', views.student_report, name='students_report'),
]
