from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from v1.apps.v1_users.models import User


class CourseStatus(models.IntegerChoices):
    OPEN = 1, 'open'
    CLOSED = 2, 'closed'
    AVAILABLE = 3, 'available'


class CourseLevel(models.IntegerChoices):
    BASE = 1, 'base'
    ADVANCED = 2, 'advanced'
    EXTRA = 3, 'extra'


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    english_name = models.CharField(
        max_length=100,
        verbose_name='Название на английском'
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание'
    )
    short_description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name='Краткое описание'
    )
    status = models.IntegerField(
        choices=CourseStatus.choices,
        default=CourseStatus.CLOSED,
        verbose_name='Статус'
    )
    photo = models.ImageField(
        upload_to='course_avatars/',
        null=True,
        blank=True,
        verbose_name='Фото'
    )
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=5,
        verbose_name='Рейтинг'
    )
    level = models.IntegerField(
        choices=CourseLevel.choices,
        default=CourseLevel.BASE,
        verbose_name='Уровень'
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class UserCourseStatus(models.IntegerChoices):
    LISTENER = 1, 'listener'
    CURATOR = 2, 'curator'
    ADMIN = 3, "admin"


class UserOnCourse(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс'
    )
    user_status = models.IntegerField(
        choices=UserCourseStatus.choices,
        default=UserCourseStatus.LISTENER,
        verbose_name='Статус'
    )
    date_updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = "Слушатели"
        verbose_name = 'Слушатель'
