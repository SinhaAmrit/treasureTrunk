from django.contrib import admin
from userauths.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "username", "email", "bio", "last_login", "date_joined"]

admin.site.register(User, UserAdmin)
