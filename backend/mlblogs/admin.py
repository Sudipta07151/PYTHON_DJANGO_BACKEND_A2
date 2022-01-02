from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from mlblogs.models import Users


class MyUserAdmin(UserAdmin):
    model = Users
    add_fieldsets = UserAdmin.add_fieldsets
    list_display = ('username', 'email')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )


admin.site.register(Users, MyUserAdmin)
