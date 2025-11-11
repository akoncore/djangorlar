from django.contrib import admin
from typing import Optional
from django.core.handlers.wsgi import WSGIRequest
from .models import (User,Restaurant,Option,MenuItem,Category,ItemCategory,Order,ItemOption,PromoCode,OrderCode,Address,OrderItem)
# Register your models here.



@admin.register(Restaurant)
class AdminRestaurant(admin.ModelAdmin):
    list_display = ("name","description","image")
    list_editable = ("description","image",)
    list_filter = ("created_at","updated_at",)
    list_display_links = ("name",)
    ordering = ("-updated_at",)
    list_filter = ("updated_at",)
    
    fieldsets = ((
        "Restaurant information",
        {
            "fields":(
                "name",
                "description",
                "image"
            )
        }
    ),
    (
        "Date and Time Information",
        {
            "fields":(
                "created_at",
                "updated_at"
            )
        }
    ))
    readonly_fields = (
        "created_at",
        "updated_at",
        "deleted_at",
    )
    
    def has_add_permission(self, request:WSGIRequest)->bool:
        return False
    
    
    def has_delete_permission(self, request:WSGIRequest, obj:Optional[Restaurant]= None)->bool:
        return False
    
    def has_change_permission(self, request, obj:Optional[Restaurant]= None):
        return False
    
