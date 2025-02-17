from django.db import models
from .base_model import BaseModel
from django.shortcuts import reverse


class User(BaseModel):
    ROLE_CHOICES = [
        ('p', 'Преподаватель'),
        ('s', 'Студент'),
        ('a', 'Администратор'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default='s', blank=True)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

    def is_teacher(self):
        return self.role == 'p'