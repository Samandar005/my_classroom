from django.db import models
from .base_model import BaseModel
from django.shortcuts import reverse


class User(BaseModel):
    ROLE_CHOICES = [
        ('p', 'Преподаватель'),
        ('s', 'Студент'),
        ('a', 'Администратор'),
    ]

    CHOICES_STATUS = [
        ('ac', 'Активный'),
        ('in', 'Неактивный'),
        ('pd', 'В ожидании'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default='s', blank=True)
    status = models.CharField(max_length=2, choices=CHOICES_STATUS, default='in')
    image = models.ImageField(upload_to='users/')
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

    def is_teacher(self):
        return self.role == 'p'

    def get_update_url(self):
        return reverse('users:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('users:delete', args=[self.pk])

