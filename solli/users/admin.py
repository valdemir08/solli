from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Campos adicionais que você tenha em User, por exemplo:
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('full_name', 'document', 'document_type', 'is_company')}),
    )

    # Também para mostrar na listagem
    list_display = BaseUserAdmin.list_display + ('full_name', 'document', 'document_type', 'is_company')