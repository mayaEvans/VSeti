# Generated by Django 3.2.3 on 2022-01-25 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1_courses', '0005_alter_useroncourse_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useroncourse',
            name='status',
            field=models.IntegerField(choices=[(1, 'listener'), (2, 'curator'), (3, 'admin')], default=1),
        ),
    ]
