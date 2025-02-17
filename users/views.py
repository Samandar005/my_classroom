from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import UserForm
from .models import User

class HomePageView(View):
    def get(self, request):
        return render(request, 'index.html')

class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'users/users.html', {'users': users})

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
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserForm(instance=user)
        return render(request, 'users/users-form.html', {'form': form})

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:list')
        return render(request, 'users/users-form.html', {'form': form})

class UserDeleteView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        return render(request, 'users/users-delete-confirm.html' ,{'user': user})

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return redirect('users:list')

