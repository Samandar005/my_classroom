from django.shortcuts import render, redirect
from django.views import View
from .models import Course
from .forms import CourseForm


class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'courses/courses.html', {'courses': courses})

class CreateCourseView(View):
    def get(self, request):
        form = CourseForm()
        return render(request, 'courses/course-form.html', {'form':form, 'user': None})

    def post(self, request):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:list')
        return render(request, 'courses/course-form.html', {'form': form})

