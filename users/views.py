from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import UserForm


class HomePageView(View):
    def get(self, request):
        return render(request, 'index.html')

class UserCreateView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'users/users-form.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:list')
        return render(request, 'users/users-form.html', {'form': form})

class UserUpdateView(View):
    def get(self):

    def post(self):



