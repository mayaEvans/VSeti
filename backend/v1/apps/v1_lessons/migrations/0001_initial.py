# Generated by Django 3.1.3 on 2022-03-16 17:42

import ckeditor.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('theory', ckeditor.fields.RichTextField()),
                ('task', ckeditor.fields.RichTextField()),
                ('task_points', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('status', models.IntegerField(choices=[(1, 'not viewed'), (2, 'viewed')], default=1)),
                ('date_posted', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
