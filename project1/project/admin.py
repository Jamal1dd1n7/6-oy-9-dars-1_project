from django.contrib import admin
from .models import Course, Lesson

admin.site.register(Course)

class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'duration', 'created_at', 'course')
    list_display_links = ('id', 'title')
    list_editable = ('course',)
    list_filter = ('course',)
    search_fields = ('title',)
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = False
    save_on_top = False

admin.site.register(Lesson, LessonAdmin)