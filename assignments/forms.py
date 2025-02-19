from django import forms
from .models import Assignment
from django.core.exceptions import ValidationError
from datetime import date

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('name', 'course', 'description', 'due_date', 'max_ball', 'status')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Введите название задания'
            }),
            'course': forms.Select(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            }),
            'description': forms.Textarea(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Введите описание задания',
                'rows': 3
            }),
            'due_date': forms.DateTimeInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'type': 'datetime-local',
            }),
            'max_ball': forms.NumberInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Максимальный балл',
            }),
            'status': forms.Select(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise ValidationError("Название задания должно содержать минимум 3 символа.")
        return name

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date.date() < date.today():
            raise ValidationError("Дата сдачи должна быть в будущем.")
        return due_date

    def clean_max_ball(self):
        max_ball = self.cleaned_data.get('max_ball')
        if max_ball < 0:
            raise ValidationError("Максимальный балл не может быть отрицательным.")
        return max_ball
