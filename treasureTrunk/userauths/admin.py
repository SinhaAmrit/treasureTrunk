from django.contrib import admin
from userauths.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "first_name",
        "email",
        "bio",
        "last_login",
        "date_joined",
    ]


admin.site.register(User, UserAdmin)
