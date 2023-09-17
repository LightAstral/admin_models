from django.shortcuts import render
from .models import Teacher, Course, Student


# Create your views here.

def home(request):
    return render(request, 'itstep/home.html')


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'itstep/teacher_list.html', {'teachers': teachers})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'itstep/course_list.html', {'courses': courses})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'itstep/student_list.html', {'students': students})
