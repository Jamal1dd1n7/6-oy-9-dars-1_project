from django.urls import path
from .views import home, course, lesson, add_lesson, add_course

urlpatterns = [
    path('', home, name='home'),
    path('course/<int:course_id>/', course, name='course_by_type'),
    path('lesson/<int:lesson_id>/', lesson, name='lesson_detail'),
    path('lesson/add/', add_lesson, name='add_lesson'),
    path('course/add/', add_course, name='add_course'),
]