# Generated by Django 3.1.3 on 2022-05-02 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v1_courses', '0018_auto_20220502_1201'),
        ('v1_certificates', '0005_auto_20220413_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='certificate',
        ),
        migrations.AddField(
            model_name='certificate',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='v1_courses.course', verbose_name='Курс'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certificate',
            name='date_added',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
    ]
