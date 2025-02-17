from django.shortcuts import render
from django.views import View
from .models import Course
from .forms import CourseForm


class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'courses/courses.html', {'courses': courses})

class CreateCourseView(View):
    def get(self, request):


    def post(self, request):
