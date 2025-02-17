from django.shortcuts import render
from django.views import View
from .models import Course


class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'courses/courses.html', {'courses': courses})


