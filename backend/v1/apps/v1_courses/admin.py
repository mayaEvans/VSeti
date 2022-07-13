from admin_numeric_filter.admin import RangeNumericFilter
from django.contrib import admin
from django.contrib.admin.actions import delete_selected
from django.utils.safestring import mark_safe

from v1.apps.v1_courses.models import Course, UserOnCourse


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'rating', 'listeners','level')
    list_filter = ('status', ('rating', RangeNumericFilter), 'level')
    search_fields = ('name', 'short_description', 'description')
    ordering = ('rating', 'name','level')
    list_per_page = 10
    list_editable = ('status',)

    fieldsets = (
        (None, {
            'fields':
                ('name', 'english_name', 'status', 'level')
        }),
        ('Описание', {
            'fields':
                ('short_description', 'description')
        }),
        ('Фото', {
            'fields':
                ('photo', 'image_photo')
        })
    )
    readonly_fields = ['image_photo']

    def image_photo(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.photo.url,
            width="200px",
            height="100px",
        )
        )

    image_photo.short_description = "Предпросмотр"

    def listeners(self, queryset):
        try:
            listeners = UserOnCourse.objects.filter(course=queryset.id).count()
            return listeners
        except UserOnCourse.DoesNotExist:
            return 0

    listeners.short_description = "Слушатели"

    def setOpen(self, request, queryset):
        rows_updated = queryset.update(status=1)
        self.message_user(request, "У % s курсов установлен статус 'открыт'" % rows_updated)

    setOpen.short_description = "Установить статус 'открыт'"

    def setAvailable(self, request, queryset):
        rows_updated = queryset.update(status=3)
        self.message_user(request, "У % s курсов установлен статус 'доступен'" % rows_updated)

    setAvailable.short_description = "Установить статус 'доступен'"

    def setClosed(self, request, queryset):
        rows_updated = queryset.update(status=2)
        self.message_user(request, "У % s курсов установлен статус 'закрыт'" % rows_updated)

    setClosed.short_description = "Установить статус 'закрыт'"
    delete_selected.short_description = "Удалить"
    actions = (setOpen, setAvailable, setClosed)


class UserOnCourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'user_status')
    list_filter = ('user_status',)
    ordering = ('user', 'course', 'user_status')
    list_per_page = 10
    list_editable = ('user_status',)

    fieldsets = (
        (None, {
            'fields':
                ('name', 'status')
        }),
        ('Описание', {
            'fields':
                ('short_description', 'description')
        }),
        ('Фото', {
            'fields':
                ('photo', 'image_photo')
        })
    )

    def setListener(self, request, queryset):
        rows_updated = queryset.update(status=1)
        self.message_user(request, "У % s пользователей на курсе установлен статус 'слушатель'" % rows_updated)

    setListener.short_description = "Сделать слушателем"

    def setCurator(self, request, queryset):
        rows_updated = queryset.update(status=3)
        self.message_user(request, "У % s пользователей на курсе установлен статус 'куратор'" % rows_updated)

    setCurator.short_description = "Сделать куратором"

    delete_selected.short_description = "Удалить"
    actions = (setListener, setCurator)


admin.site.register(Course, CourseAdmin)
admin.site.register(UserOnCourse, UserOnCourseAdmin)
