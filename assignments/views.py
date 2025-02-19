from django.shortcuts import render
from .models import Assignment
from django.views import View


class AssignmentListView(View):
    def get(self, request):
        assignments = Assignment.objects.all()
        ctx = {'assignments': assignments}
        return render(request, 'assignments/assignments.html', ctx)

