# Generated by Django 3.2.3 on 2021-11-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
