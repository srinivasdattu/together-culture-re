from django.contrib import admin
from .models import User, Interest
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {
            'fields': ('is_approved', 'is_admin_user', 'phone', 'location', 'interests',
                       'professional_background', 'why_join', 'how_contribute')
        }),
    )
    list_display = ['username', 'email', 'is_approved', 'is_admin_user']

admin.site.register(User, CustomUserAdmin)
admin.site.register(Interest)
