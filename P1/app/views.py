from django.shortcuts import render
from .models import Student

# Student list - Get all data 
def student_list(request):
    student = Student.objects.all()
    return render(request, 'app/student.html', {'student': student})

# Student detail - Get by it's i
def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'app/student.html', {'student': student})

# Student Create
def student_detail(request):
    student = Student.objects.get()
    return render(request, 'app/student_form.html', {'student': student})

# Student update
def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'app/student_form.html', {'student': student})

# Student delete
def student_detail(request, pk):
    student = Student.objects.get(pk=pk)