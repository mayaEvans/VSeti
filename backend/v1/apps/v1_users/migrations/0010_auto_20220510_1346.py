# Generated by Django 3.1.3 on 2022-05-10 10:46

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1_users', '0009_user_date_joined'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
