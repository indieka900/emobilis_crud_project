from django.shortcuts import render, redirect, get_object_or_404
from crud_app.models import Student
from crud_app.forms import StudentForm
from django.contrib import messages


def home(request):
    students = Student.objects.all()
    return render(request, 'crud_app/home.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'crud_app/student_detail.html', {'student': student})

def add_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully.')
            return redirect('home')
    return render(request, 'crud_app/form.html', {'form': form})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully.')
            return redirect('home')
    return render(request, 'crud_app/form.html', {'form': form,'student': student})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully.')
        return redirect('home')
    return render(request, 'crud_app/student_delete.html', {'pk': pk})

# Create your views here.
