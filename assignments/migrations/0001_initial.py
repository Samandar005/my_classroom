# Generated by Django 5.1.3 on 2025-02-19 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('status', models.CharField(choices=[('ac', 'Активный'), ('in', 'Неактивный'), ('pd', 'В ожидании')], default='in', max_length=2)),
                ('max_ball', models.PositiveIntegerField(default=0)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='courses.course')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
