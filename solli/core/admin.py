from django.contrib import admin

from core.models import BaseEntryCategory, Location, Image

# Register your models here.
admin.site.register(Location)
admin.site.register(BaseEntryCategory)
admin.site.register(Image)