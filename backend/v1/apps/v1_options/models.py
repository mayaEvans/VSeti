from django.db.models import CASCADE
from django.db import models
from v1.apps.v1_questions.models import Question


class Option(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=CASCADE,
        related_name="options",
        verbose_name='Вопрос'
    )
    option = models.CharField(
        max_length=100,
        verbose_name='Вариант ответа'
    )
    is_correct = models.BooleanField(
        null=True,
        verbose_name='Правильность варианта ответа'
    )

    class Meta:
        verbose_name_plural = "Варианты ответов"
        verbose_name = "Вариант ответа"

    def __str__(self):
        return str(self.option)
