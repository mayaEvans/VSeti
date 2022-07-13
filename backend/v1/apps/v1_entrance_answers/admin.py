from django.contrib import admin

# Register your models here.
from django.contrib.admin.actions import delete_selected

from v1.apps.v1_entrance_answers.models import EntranceAnswer


class EntranceAnswerAdmin(admin.ModelAdmin):
    list_display = ('get_question', 'get_user', 'get_correct')
    list_filter = ('correct', 'entrance_question')
    ordering = ('entrance_question',)
    list_per_page = 10
    list_display_links = ('get_question',)

    def get_user(self, obj):
        return obj.user.email

    get_user.short_description = 'Пользователь'
    get_user.admin_order_field = 'user__user'

    def get_question(self, obj):
        return obj.entrance_question.text

    get_question.short_description = 'Вопрос'
    get_question.admin_order_field = 'entrance_question__entrance_question'

    def get_correct(self, obj):
        return obj.correct

    get_correct.short_description = 'Правильность'

    fieldsets = (
        (None, {
            'fields':
                ('entrance_question', 'user', 'correct')
        }),
        (None, {
            'fields':
                ('selected_options',)
        })
    )

    delete_selected.short_description = "Удалить"


admin.site.register(EntranceAnswer, EntranceAnswerAdmin)

