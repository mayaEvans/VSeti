from django.contrib import admin

# Register your models here.
from django.contrib.admin.actions import delete_selected

from v1.apps.v1_questions.models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('get_lesson', 'text')
    list_filter = ('lesson',)
    ordering = ('lesson',)
    list_per_page = 10
    list_display_links = ('text',)

    def get_lesson(self, obj):
        return obj.lesson.name

    get_lesson.short_description = 'Урок'
    get_lesson.admin_order_field = 'lesson__lesson'

    delete_selected.short_description = "Удалить"


admin.site.register(Question, QuestionAdmin)
