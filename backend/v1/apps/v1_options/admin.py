from django.contrib import admin

# Register your models here.
from django.contrib.admin.actions import delete_selected

from v1.apps.v1_options.models import Option


class OptionAdmin(admin.ModelAdmin):
    list_display = ('get_question', 'option', 'get_correct')
    list_filter = ('is_correct',)
    ordering = ('question',)
    list_per_page = 10
    list_display_links = ('option',)

    def get_question(self, obj):
        return obj.question.text

    get_question.short_description = 'Вопрос'
    get_question.admin_order_field = 'question__question'

    def get_correct(self, obj):
        return obj.is_correct

    get_correct.short_description = 'Правильность'

    delete_selected.short_description = "Удалить"


admin.site.register(Option, OptionAdmin)