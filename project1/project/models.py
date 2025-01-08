from django.db import models
from PIL import Image
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
class Course(models.Model):
    title = models.CharField(max_length=255)
    teacher = models.CharField(max_length=255, null=True)
    course_type = models.CharField(max_length=255, null=True)
    student_count = models.IntegerField(default=0)
    created_at = models.DateField(blank=True, null=True)  
    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=255)  
    teacher = models.CharField(max_length=255, null=True)
    content = models.TextField()  
    duration = models.DurationField(blank=True, null=True)  
    created_at = models.DateField(blank=True, null=True, auto_now_add=True)  
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)  

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(max_length=1000, verbose_name="Matni")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Muallif")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="Dars mavzusi")
    created = models.DateTimeField(auto_now_add=models.CASCADE, verbose_name="Yaratilgan")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Izoh "
        verbose_name_plural = "Izohlar"
        ordering = ['-id']
