from django.urls import path
from .views import *

urlpatterns = [
    # home 
    path('', home, name='home'),
    # ----------------------------------------------------------------------------------------------------------------------------------------------------
    
    # course
    path('course/<int:course_id>/', course, name='course_by_type'),
    path('course/add/', add_course, name='add_course'),
    path('course/<int:course_id>/', update_course, name='update_course'),
    path('course/<int:course_id>/', delete_course, name='delete_course'),
    # ----------------------------------------------------------------------------------------------------------------------------------------------------
    
    # lesson
    path('lesson/<int:lesson_id>/', lesson, name='lesson_detail'),
    path('lesson/add/', add_lesson, name='add_lesson'),
    path('lesson/<int:lesson_id>/', update_lesson, name='update_lesson'),
    path('lesson/<int:lesson_id>/', delete_lesson, name='delete_lesson'),
    # ----------------------------------------------------------------------------------------------------------------------------------------------------
   
    # comment
    path('lesson/<int:lesson_id>/comment/save/', comment_save, name='comment_save'),
    path('comment/<int:comment_id>/delete/', comment_delete, name='deleteComment'),
    path('comment/<int:comment_id>/update/', comment_update, name='updateComment'),
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 

    # auth
    path('auth/register/', register, name='register'),
    path('auth/login/', loginPage, name='login'),
    path('auth/logout/', logoutPage, name='logout'),
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
]