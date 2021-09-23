from django.contrib import admin
from user.models import User


class AdminUser(admin.ModelAdmin):
    list_display = (
        "show_image",
        "username",
        "is_staff",
        "is_active",
    )
    readonly_fields = ("username", "last_login")
    list_filter = ("is_staff",)
    search_fields = ("username",)

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password",
                    "is_staff",
                    "last_login",
                )
            },
        ),
    )


admin.site.register(User, AdminUser)
