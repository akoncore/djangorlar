from rest_framework.viewsets import ViewSet
from rest_framework import status,permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import (
    Course,
    Lesson
)
from .serializers import (
    CourseListSerializer
)

class CourseListView(ViewSet):
    def list(self,request):
        queryset = Course.objects.filter(is_active = True)
        serializer = CourseListSerializer(queryset,many=True)
        return Response(serializer.data)
    