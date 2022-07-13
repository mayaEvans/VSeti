from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import CASCADE

from v1.apps.v1_courses.models import Course, UserOnCourse


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=CASCADE,
        verbose_name='Курс'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    theory = RichTextField(
        verbose_name='Теория')
    order = models.IntegerField(
        default=1,
        verbose_name='Сортировка'
    )
    date_posted = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата публикации'
    )

    class Meta:
        verbose_name_plural = "Уроки"
        verbose_name = 'Урок'

    def __str__(self):
        return self.name
