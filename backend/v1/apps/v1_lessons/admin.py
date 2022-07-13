from django.contrib import admin

from v1.apps.v1_lessons.models import Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_course', 'date_posted')
    list_filter = ('date_posted',)
    search_fields = ('name',)
    ordering = ('date_posted', 'course')
    list_per_page = 10

    def get_course(self, obj):
        return obj.course.name

    get_course.short_description = 'Курс'

    fieldsets = (
        (None, {
            'fields':
                ('name', 'course', 'order')
        }),
        ('Содержание', {
            'fields':
                ('theory',)
        }),
    )


admin.site.register(Lesson, LessonAdmin)
