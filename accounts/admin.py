from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('ポイント情報', {'fields': ('points',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('ポイント情報', {'fields': ('points',)}),
    )
    list_display = UserAdmin.list_display + ('points',)

admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.



