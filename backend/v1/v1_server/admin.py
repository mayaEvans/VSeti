from django.contrib import admin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token

admin.site.site_header = '#ВСЕТИ'
admin.site.index_title = 'Раздел администрирования'
admin.site.site_title = "Администрирование #ВСЕТИ"

# admin.site.unregister(Token)
# admin.site.unregister(Group)
