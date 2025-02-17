from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'code', 'description', 'status', 'teacher', 'due_date')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Название курса должно содержать не менее 3 символов.")
        return name

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if len(code) < 5:
            raise forms.ValidationError("Код курса должен содержать не менее 5 символов.")
        if not code.isalnum():
            raise forms.ValidationError("Код курса должен содержать только буквы и цифры.")
        return code

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
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
