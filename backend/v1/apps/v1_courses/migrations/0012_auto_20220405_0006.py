# Generated by Django 3.1.3 on 2022-04-04 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1_courses', '0011_auto_20220404_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.IntegerField(choices=[(1, 'открыт'), (2, 'закрыт'), (3, 'доступен')], default=1),
        ),
    ]
