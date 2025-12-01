from rest_framework.serializers import (
    Serializer,
    ModelSerializer,
    SerializerMethodField
)
from .models import (
    Course,
    Lesson
)

class CourseListSerializer(ModelSerializer):
    owner_info = SerializerMethodField()
    
    class Meta:
        model = Course
        fields = [
            'title',
            'description',
            'is_active',
            'owner_info',
            'created_at'
        ]
    
    def get_owner_info(self,obj):
        owner = obj.owner
        return{
            'id':owner.id,
            'full_name':owner.full_name
        }

class CourseCreateSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'title',
            'description',
        ]

class LessonSerializer(ModelSerializer):
    course_info = SerializerMethodField()
    
    class Meta:
        model = Lesson
        fields = [
            'title',
            'content',
            'order',
            'indentation',
            'is_published',
            'course_info'
        ]
        
    def get_course_info(self,obj):
        course = obj.course
        return{
            'id':course.id,
            'title':course.title,
            'owner':course.owner
        }
        
class LessonsCreateSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'title',
            'content',
            'course'
        ]
    
    
class IsPublishedLessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'is_published'
        ]