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
        return render(request, 'courses/course-form.html', {'form': form, 'user': None})

    def post(self, request):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:list')
        return render(request, 'courses/course-form.html', {'form': form})

class UpdateCourseView(View):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        form = CourseForm(instance=course)
        return render(request, 'courses/course-form.html', {'form': form, 'course': course})

    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        form = CourseForm(request.POST)

        if form.is_valid():
            course.name = form.cleaned_data.get('name', course.name)
            course.code = form.cleaned_data.get('code', course.code)
            course.description = form.cleaned_data.get('description', course.description)
            course.status = form.cleaned_data.get('status', course.status)
            course.teacher = form.cleaned_data.get('teacher', course.teacher)
            course.due_date = form.cleaned_data.get('due_date', course.due_date)

            course.save()
            return redirect('courses:list')

        return render(request, 'courses/course-form.html', {
            'form': form,
            'course': course,
            'errors': form.errors,
            'error_message': 'Kursni yangilashda xato yuz berdi. Iltimos, barcha maydonlarni to\'g\'ri to\'ldiring.'
        })


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