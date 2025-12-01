from django.urls import path,include
from .views import (
    CourseListView,
    LessonView
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'courses',CourseListView,basename='courses')
router.register(r'lessons',LessonView,basename='lessons')

urlpatterns = [
    path('v1/',include(router.urls))
]


