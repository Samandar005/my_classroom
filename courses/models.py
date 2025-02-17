from django.db import models
from django.shortcuts import reverse
from users.base_model import BaseModel
from users.models import User

class Course(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name

    def is_teacher(self):
        return self.teacher.role == 'p'