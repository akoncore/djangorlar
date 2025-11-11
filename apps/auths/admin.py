from django.contrib.admin import register, ModelAdmin
from apps.auths.models import CustomUser

@register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    list_display = (
    'email', 
    'first_name',
    'last_name',
    'city',
    'birth_date',
    'salary',
    'department',
    'role',
    'is_active',
    'is_staff',
    'is_superuser',
    'created_at',
    )
    search_fields = ('email','department','role')
    list_filter = ('is_active', 'is_staff', 'is_superuser','date_joined','last_login',)
    ordering = ('email',) 

# Register your models here.
