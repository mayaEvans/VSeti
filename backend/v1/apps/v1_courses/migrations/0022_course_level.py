# Generated by Django 3.1.3 on 2022-05-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1_courses', '0021_auto_20220510_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.IntegerField(choices=[(1, 'base'), (2, 'advanced'), (3, 'extra')], default=1, verbose_name='Уровень'),
        ),
    ]