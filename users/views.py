from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import UserForm
from .models import User
from courses.models import Course


class HomePageView(View):
    def get(self, request):
        ac_courses_count = Course.objects.filter(status='ac').count()
        ctx = {
            'ac_courses_count': ac_courses_count,

        }
        return render(request, 'index.html', ctx)

class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        ctx = {'users': users}
        return render(request, 'users/users.html', ctx)

class UserCreateView(View):
    def get(self, request):
        form = UserForm()
        ctx = {'form': form, 'user': None}
        return render(request, 'users/users-form.html', ctx)

    def post(self, request):
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:list')
        ctx = {'form': form}
        return render(request, 'users/users-form.html', ctx)

class UserUpdateView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserForm(instance=user)
        ctx = {'form': form, 'user': user}
        return render(request, 'users/users-form.html', ctx)

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user.name = form.cleaned_data.get('name')
            user.email = form.cleaned_data.get('email')
            user.role = form.cleaned_data.get('role')
            user.status = form.cleaned_data.get('status')
            user.image = form.cleaned_data.get('image')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 and password1 == password2:
                user.set_password(password1)
            user.save()
            return redirect('users:list')
        ctx = {'form': form, 'user': user}
        return render(request, 'users/users-form.html', ctx)

class UserDeleteView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        ctx = {'user': user}
        return render(request, 'users/users-delete-confirm.html' ,ctx)

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return redirect('users:list')

