from django.db import models
from django.shortcuts import reverse
from courses.models import Course
from users.base_model import BaseModel


class Assignment(BaseModel):
    name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments', null=True, blank=True)
    description = models.TextField()
    due_date = models.DateField()
    max_ball = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name}"
