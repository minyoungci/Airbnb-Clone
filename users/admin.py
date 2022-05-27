from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rooms import models as room_models
from . import models

# Register your models here.


class Roominline(admin.TabularInline):
    model = room_models.Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    inlines = (Roominline,)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
        "email_verified",
        "email_secret",
        "login_method",
    )
