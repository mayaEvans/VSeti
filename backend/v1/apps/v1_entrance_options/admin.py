from django.contrib import admin

# Register your models here.
from django.contrib.admin.actions import delete_selected

from v1.apps.v1_entrance_options.models import EntranceOption


class EntranceOptionAdmin(admin.ModelAdmin):
    list_display = ('get_entrance_question', 'option', 'get_correct')
    list_filter = ('is_correct',)
    ordering = ('entrance_question',)
    list_per_page = 10
    list_display_links = ('option',)

    def get_entrance_question(self, obj):
        return obj.entrance_question.text

    get_entrance_question.short_description = 'Вопрос для входного тестирования'
    get_entrance_question.admin_order_field = 'entrance_question__entrance_question'

    def get_correct(self, obj):
        return obj.is_correct

    get_correct.short_description = 'Правильность'

    delete_selected.short_description = "Удалить"


admin.site.register(EntranceOption, EntranceOptionAdmin)
