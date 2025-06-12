from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'full_name', 'is_company', 'cnpj', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'full_name', 'cnpj')
    ordering = ('username',)

    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('full_name', 'is_company', 'cnpj')}),
    )

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('full_name', 'is_company', 'cnpj')}),
    )