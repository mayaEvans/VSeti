from django.db import models
from django.db.models import CASCADE

from v1.apps.v1_courses.models import UserOnCourse
from v1.apps.v1_entrance_options.models import EntranceOption
from v1.apps.v1_entrance_questions.models import EntranceQuestion
from v1.apps.v1_options.models import Option
from v1.apps.v1_questions.models import Question
from v1.apps.v1_users.models import User


class EntranceAnswer(models.Model):
    entrance_question = models.ForeignKey(
        EntranceQuestion,
        on_delete=CASCADE,
        verbose_name='Вопрос из входного тестирования'
    )
    user = models.ForeignKey(
        User,
        on_delete=CASCADE,
        verbose_name='Пользователь'
    )
    selected_options = models.ManyToManyField(
        EntranceOption,
        related_name="selected_options",
        verbose_name='Выбранные варианты ответа'
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
