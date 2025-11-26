from django.contrib.admin import(
    register,
    ModelAdmin
) 
from .models import (
    Course,
    Lesson
)

@register(Course)
class CourseAdmin(ModelAdmin):
    list_display = ('title','description','is_active','owner','created_at',)
    list_display_links = ('title',)
    list_editable = ('is_active',)
    list_filter = ('is_active','owner',)
    ordering = ('-created_at',)
    
    
@register(Lesson)
class LessonAdmin(ModelAdmin):
    list_display = ('course','title','order','is_published',)
    list_display_links = ('course',)
    list_editable = ('is_published',)
    list_filter = ('course',)
    ordering = ('-created_at',)
    
    