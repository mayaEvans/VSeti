# Generated by Django 3.1.3 on 2022-02-24 17:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1_courses', '0007_auto_20220214_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='listeners_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='rating',
            field=models.FloatField(default=5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]