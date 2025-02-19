from django.shortcuts import render, redirect, get_object_or_404
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
        return render(request, 'courses/course-form.html', {'form': form})

    def post(self, request):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:list')
        ctx = {'form': form}
        return render(request, 'courses/course-form.html', ctx )

class UpdateCourseView(View):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        form = CourseForm(instance=course)
        ctx = {'form': form, 'course': course}
        return render(request, 'courses/course-form.html', ctx)

    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses:list')
        ctx = {'form': form, 'course': course}
        return render(request, 'courses/course-form.html', ctx)


class CourseDeleteView(View):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        return render(request, 'courses/course-delete-confirm.html' ,{'course': course})

    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return redirect('courses:list')

class CourseDetailView(View):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        return render(request, 'courses/course-details.html', {'course': course})