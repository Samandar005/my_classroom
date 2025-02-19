from django.db import models
from django.shortcuts import reverse
from courses.models import Course
from users.base_model import BaseModel
from django.utils.text import slugify


class Assignment(BaseModel):
    CHOICES_STATUS = [
        ('ac', 'Активный'),
        ('in', 'Неактивный'),
        ('pd', 'В ожидании'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=2, choices=CHOICES_STATUS, default='in')
    max_ball = models.PositiveIntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Assignment, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('assignments:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])


    def __str__(self):
        return f"{self.name}"
