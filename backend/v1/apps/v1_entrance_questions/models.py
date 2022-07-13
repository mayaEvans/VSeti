from ckeditor.fields import RichTextField
from django.db import models


class EntranceQuestion(models.Model):
    text = RichTextField(
        verbose_name='Текст вопроса'
    )

    class Meta:
        verbose_name_plural = "Вопросы для входного тестирования"
        verbose_name = "Вопрос для входного тестирования"

    def __str__(self):
        return str(self.text)
