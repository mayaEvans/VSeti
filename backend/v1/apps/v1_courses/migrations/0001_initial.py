# Generated by Django 3.2.3 on 2021-11-14 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('short_description', models.TextField(blank=True, max_length=500, null=True)),
                ('status', models.IntegerField(choices=[(1, 'open'), (2, 'closed'), (3, 'available')], default=1)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='course_avatars/')),
            ],
        ),
        migrations.CreateModel(
            name='UserCourseStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'listener'), (2, 'admin'), (3, 'curator'), (4, 'archived'), (5, 'passed')], default=1)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserOnCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1_courses.course')),
            ],
        ),
    ]
