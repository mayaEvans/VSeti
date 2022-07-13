from django.contrib import admin

# Register your models here.
from v1.apps.v1_reviews.models import Review

admin.site.register(Review)
