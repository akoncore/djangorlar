from argparse import Action
from rest_framework.viewsets import ViewSet
from rest_framework import status,permissions
from rest_framework.decorators import permission_classes,action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.serializers import ValidationError

from .models import (
    Course,
    Lesson
)
from .serializers import (
    CourseListSerializer,
    CourseCreateSerializer,
    LessonSerializer,
    LessonsCreateSerializer,
    IsPublishedLessonSerializer
)

class CourseListView(ViewSet):
    def list(self,request):
        queryset = Course.objects.filter(is_active = True)
        serializer = CourseListSerializer(queryset,many=True)
        permission_classes = [permissions.AllowAny]
        return Response(serializer.data)
    
    
    def post(self,request):
        queryset = Course.objects.all()
        serializer = CourseCreateSerializer(queryset,many=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data ,status=status.HTTP_201_CREATED)
    
    
    def retrieve(self,requset,pk=None):
        queryset = Course.objects.all()
        course = get_object_or_404(queryset,pk=pk)
        serializer = CourseListSerializer(course)
        return Response(serializer.data)
    
    def update(self,request,pk=None):
        course = Course.objects.get(pk=pk)
        serializer = CourseListSerializer(course,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,status=status.HTTP_201_CREATED
            )
        else:
            return Response({
                'message':'Error'
            })
            
    def delete(self,request, pk=None):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
    
    @action(detail=True,methods=["Get"])
    def activate(self,request,pk=None):
        course = Course.objects.get(pk=pk)
        
        if not course.is_active:
            course.is_active = True
            course.save()
            
        serializer = CourseListSerializer(course)
        return Response(serializer.data)
        
    
    @action(detail=True,methods=['Get'])
    def deactivate(self,request,pk=None):
        course = Course.objects.get(pk=pk)
        if course.is_active:
            course.is_active = False
            course.save()
        
        serializer = CourseListSerializer(course)
        
        return Response(
            serializer.data
        )
       
    @action(detail=True,methods=['get'])
    def lessons(self,request,pk =None):
        course = Course.objects.get(pk = pk)
        lesson = course.lessons.all()
        serializer = CourseListSerializer(lesson,many = True)
        return Response(serializer.data)
            
            
class LessonView(ViewSet):
    
    
    
    def create(self,request):
        serializer = LessonsCreateSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response( serializer.data, status=status.HTTP_201_CREATED)
         
         
    def delete(self,pk=None):
        lesson = Lesson.objects.get(pk=pk)
        lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    @action(detail=True,methods=['post'])
    def publish(self,request,pk=None):
        lesson = self.get_objects()
        serliazer = IsPublishedLessonSerializer(lesson,data = {'is_published':True},partial = True)
        serliazer.is_valid(raise_exception=True)
        serliazer.save()
        return Response(serliazer.data)
        