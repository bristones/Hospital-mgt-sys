from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email','username','staff_id','name','mobile_number','is_active','is_staff')
    search_fields = ('email','username','mobile_number')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('name','email','mobile_number', 'staff_id')}),
        ('Permissions', {'fields': ('is_active','is_staff','is_superuser','groups','user_permissions')}),
    )

admin.site.register(CustomUser,CustomUserAdmin)
