from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser, SocialMedia, MetaDetails
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "name", "dob", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "name", "dob", "password1", "password2", "is_staff", "is_superuser",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email", "name")
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)