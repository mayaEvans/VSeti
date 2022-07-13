from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from v1.apps.v1_courses.models import UserOnCourse, Course


class Review(models.Model):
    user = models.ForeignKey(
        UserOnCourse,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс'
    )
    text = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name='Текст'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=5,
        verbose_name='Рейтинг'
    )

    class Meta:
        verbose_name_plural = "Отзывы"
        verbose_name = 'Отзыв'
