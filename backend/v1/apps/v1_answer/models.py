from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import CASCADE

from v1.apps.v1_courses.models import UserOnCourse
from v1.apps.v1_options.models import Option
from v1.apps.v1_questions.models import Question


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=CASCADE,
        verbose_name='Вопрос'
    )
    user = models.ForeignKey(
        UserOnCourse,
        on_delete=CASCADE,
        verbose_name='Слушатель'
    )
    selected_options = models.ManyToManyField(
        Option,
        related_name="selected_options",
        blank=True,
        verbose_name='Выбранные варианты ответа'
    )
    text = RichTextField(
        null=True,
        blank=True,
        verbose_name='Текст ответа'
    )
    correct = models.BooleanField(
        null=True,
        verbose_name='Правильность ответа'
    )

    class Meta:
        verbose_name_plural = "Ответы"
        verbose_name = "Ответ"

    def __str__(self):
        return str(self.selected_options)
