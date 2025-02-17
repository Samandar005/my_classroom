from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'code', 'description', 'status', 'teacher', 'due_date')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Введите название курса'
            }),
            'code': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Введите код курса'
            }),
            'description': forms.Textarea(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'placeholder': 'Введите описание курса',
                'rows': 4
            }),
            'status': forms.Select(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            }),
            'teacher': forms.Select(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
                'type': 'date'
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or len(name) < 3:
            raise forms.ValidationError("Название курса должно содержать не менее 3 символов.")
        return name

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if not code or len(code) < 5:
            raise forms.ValidationError("Код курса должен содержать не менее 5 символов.")
        if not code.isalnum():
            raise forms.ValidationError("Код курса должен содержать только буквы и цифры.")
        return code

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description or len(description) < 10:
            raise forms.ValidationError("Описание должно содержать не менее 10 символов.")
        return description

    def clean_status(self):
        status = self.cleaned_data.get('status')
        if status not in dict(Course.CHOICES_STATUS):
            raise forms.ValidationError("Выбран недопустимый статус курса.")
        return status

    def clean_teacher(self):
        teacher = self.cleaned_data.get('teacher')
        if teacher and teacher.role != 'p':
            raise forms.ValidationError("Выбранный преподаватель должен иметь роль 'Преподаватель'.")
        return teacher

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < forms.DateField().clean('1900-01-01'):
            raise forms.ValidationError("Дата окончания должна быть позже указанной даты.")
        return due_date