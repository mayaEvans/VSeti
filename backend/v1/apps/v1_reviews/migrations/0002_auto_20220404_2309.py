# Generated by Django 3.1.3 on 2022-04-04 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1_reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name_plural': 'Отзывы'},
        ),
    ]