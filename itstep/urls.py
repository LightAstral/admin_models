from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('courses/', views.course_list, name='course_list'),
    path('students/', views.student_list, name='student_list'),
]
