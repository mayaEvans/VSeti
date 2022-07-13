# Register your models here.
from django.contrib import admin
from django.contrib.admin.actions import delete_selected

from v1.apps.v1_entrance_questions.models import EntranceQuestion


class EntranceQuestionAdmin(admin.ModelAdmin):
    list_display = ('text',)
    list_per_page = 10
    list_display_links = ('text',)

    delete_selected.short_description = "Удалить"


admin.site.register(EntranceQuestion, EntranceQuestionAdmin)
