from django.contrib import admin
# Register your models here.
from django.utils.safestring import mark_safe

from v1.apps.v1_users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('image_photo',
                    'get_fullname',
                    'email',
                    'social_networks',
                    'birth_date',
                    'platform',
                    'city'
                    )
    list_filter = ('birth_date', 'platform', 'city')
    search_fields = ('first_name', 'last_name', 'social_networks', 'email')
    ordering = ('birth_date',)
    list_per_page = 10
    list_display_links = ('image_photo', 'get_fullname')

    def get_fullname(self, obj):
        if obj.last_name + obj.first_name + obj.patronymic:
            fullname = obj.last_name + " " + obj.first_name[0] + ". " + obj.patronymic[0] + ". "
            return fullname

    get_fullname.short_description = 'ФИО'

    fieldsets = (
        ('Основная информация', {
            'fields':
                (('first_name', 'last_name', 'patronymic',), 'birth_date', ('big_image_photo', 'photo'))
        }),
        ('Управление ролями', {
            'classes': ('collapse',),
            'fields':
                (('is_staff', 'is_superuser'), 'groups')
        }),
        ('Контакты', {
            'fields':
                ('email', 'social_networks')
        }),
        ('Дополнительная инфораация', {
            'fields':
                ('level', 'platform', 'city'),
        })
    )
    readonly_fields = ['image_photo', 'big_image_photo']

    def image_photo(self, obj):
        if obj.photo:
            return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.photo.url,
                width="30px",
                height="30px",
            )
            )

    image_photo.short_description = "Фото"

    def big_image_photo(self, obj):
        if obj.photo:
            return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.photo.url,
                width="70px",
                height="70px",
            )
            )

    big_image_photo.short_description = ""


admin.site.register(User, UserAdmin)
