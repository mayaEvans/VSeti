from django.contrib import admin

# Register your models here.
from v1.apps.v1_certificates.models import Certificate

admin.site.register(Certificate)
