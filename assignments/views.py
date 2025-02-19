from django.shortcuts import render, redirect, get_object_or_404
from .forms import AssignmentForm
from .models import Assignment
from django.views import View


class AssignmentListView(View):
    def get(self, request):
        assignments = Assignment.objects.all()
        ctx = {'assignments': assignments}
        return render(request, 'assignments/assignments.html', ctx)

class AssignmentCreateView(View):
    def get(self, request):
        form = AssignmentForm()
        ctx = {'form': form}
        return render(request, 'assignments/assignments-form.html', ctx)

    def post(self, request):
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignments:list')
        ctx = {'form': form}
        return render(request, 'assignments/assignments-form.html', ctx)

class AssignmentUpdateView(View):
    def get(self, request, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        form = AssignmentForm(instance=assignment)
        ctx = {'form': form, 'assignment': assignment}
        return render(request, 'assignments/assignments-form.html', ctx)

    def post(self, request, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('assignments:list')
        ctx = {'form': form, 'assignment': assignment}
        return render(request, 'assignments/assignments-form.html', ctx)
