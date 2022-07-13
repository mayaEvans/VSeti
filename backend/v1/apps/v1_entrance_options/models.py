from django.db import models
from django.db.models import CASCADE

from v1.apps.v1_entrance_questions.models import EntranceQuestion
from v1.apps.v1_questions.models import Question


class EntranceOption(models.Model):
    entrance_question = models.ForeignKey(
        EntranceQuestion,
        on_delete=CASCADE,
        related_name="options",
        verbose_name='Вопрос из входного тестирования'
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
        verbose_name_plural = "Варианты ответов для входного тестирования"
        verbose_name = "Вариант ответа для входного тестирования"

    def __str__(self):
        return str(self.option)
