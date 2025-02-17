from django.db import models
from django.shortcuts import reverse
from users.base_model import BaseModel
from users.models import User

class Course(BaseModel):
    CHOICES_STATUS = [
        ('ac', 'Активный'),
        ('in', 'Неактивный'),
        ('pd', 'В ожидании'),
    ]

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=CHOICES_STATUS, default='in')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses', null=True, blank=True)

    def __str__(self):
        return self.name

    def is_teacher(self):
        return self.teacher.role == 'p'