# Generated by Django 3.1.3 on 2022-05-10 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1_courses', '0019_auto_20220510_1326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useroncourse',
            options={'permissions': (('curator', 'curator'),), 'verbose_name': 'Слушатель', 'verbose_name_plural': 'Слушатели'},
        ),
    ]
