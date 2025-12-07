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
