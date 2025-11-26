from django.urls import path
from .views import CourseListView


urlpatterns = [
    path('courses/', view=CourseListView.as_view({'get':'list'}), name='list course')
]
