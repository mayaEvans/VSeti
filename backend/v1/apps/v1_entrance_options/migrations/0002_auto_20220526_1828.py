# Generated by Django 3.1.3 on 2022-05-26 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1_entrance_options', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entranceoption',
            options={'verbose_name': 'Вариант ответа для входного тестирования', 'verbose_name_plural': 'Варианты ответов для входного тестирования'},
        ),
    ]
