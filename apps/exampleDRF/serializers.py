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