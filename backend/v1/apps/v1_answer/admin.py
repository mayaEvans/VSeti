from django.contrib import admin
# Register your models here.
from django.contrib.admin.actions import delete_selected

from v1.apps.v1_answer.models import Answer


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('get_question', 'get_user', 'get_correct')
    list_filter = ('correct', 'question')
    ordering = ('question',)
    list_per_page = 10
    list_display_links = ('get_question',)

    def get_user(self, obj):
        return obj.user.user.email

    get_user.short_description = 'Слушатель'
    get_user.admin_order_field = 'user__user'

    def get_question(self, obj):
        return obj.question.text

    get_question.short_description = 'Вопрос'
    get_question.admin_order_field = 'question__question'

    def get_correct(self, obj):
        return obj.correct

    get_correct.short_description = 'Правильность'

    fieldsets = (
        (None, {
            'fields':
                ('question', 'user', 'correct')
        }),
        (None, {
            'fields':
                ('selected_options', 'text')
        })
    )

    delete_selected.short_description = "Удалить"


admin.site.register(Answer, AnswerAdmin)
