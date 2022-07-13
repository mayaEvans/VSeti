from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import CASCADE

from v1.apps.v1_courses.models import UserOnCourse
from v1.apps.v1_lessons.models import Lesson


class Question(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=CASCADE,
        verbose_name='Урок'
    )
    text = RichTextField(
        verbose_name='Вопрос'
    )

    class Meta:
        verbose_name_plural = "Вопросы"
        verbose_name = "Вопрос"

    def __str__(self):
        return str(self.text)
