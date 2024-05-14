from django.shortcuts import render, redirect
from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']

def course_page(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'delete':
            course.delete()
            return redirect('course_page')
    return render(request, 'delete_course.html', {'course': course})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_page')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})
