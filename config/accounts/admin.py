from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from .models import User

class UserAdmin(BaseUserAdmin):
    
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ("email", "first_name", "last_name", "phone_number")
    list_filter = ("is_admin", "is_active")
    search_fields = ("email", "first_name", "last_name")
    
    add_fieldsets = (
        (None,{"fields": ("email", "first_name", "last_name", "phone_number","password1", "password2")}),
    )
    fieldsets = (
        (None,{"fields": ("email", "first_name", "last_name", "phone_number","password")}),
        ("permissions",{"fields": ("is_admin", "is_active", "last_login")}),
    )
    
    ordering = ("first_name",)
    
    readonly_fields = ("last_login",)
    filter_horizontal = ()

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)