from django.db import models

from v1.apps.v1_courses.models import UserOnCourse, Course


class Certificate(models.Model):
    user = models.ForeignKey(
        UserOnCourse,
        on_delete=models.CASCADE,
        verbose_name='Слушатель'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.DO_NOTHING,
        verbose_name='Курс'
    )
    progress = models.IntegerField(
        default=0
    )
    date_added = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name_plural = "Сертификаты"
        verbose_name = 'Сертификат'
