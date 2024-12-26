from django.shortcuts import render, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest
from .models import Course, Lesson
from .forms import LessonForm, CourseForm

def home(request: WSGIRequest):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'intex.html', context)

def course(request: WSGIRequest, course_id):
    lessons = Lesson.objects.all()
    context = {
        'lessons': lessons
    }
    return render(request, 'course.html', context)
    
def lesson(request: WSGIRequest, lesson_id):
    lesson = get_object_or_404(Lesson, id= lesson_id)
    context = {
        'lesson': lesson
    }
    return render(request, 'lesson.html', context)
    
def add_lesson(request: WSGIRequest):

    if request.method == 'POST':
        form = LessonForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = Lesson.objects.create(**form.cleaned_data)
            print(post, "qo'shildi!")

    form = LessonForm()
    context = {
        "form": form
    }
    return render(request, 'add_lesson.html', context)

def add_course(request: WSGIRequest):

    if request.method == 'POST':
        form = CourseForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = Course.objects.create(**form.cleaned_data)
            print(post, "qo'shildi!")
        else:
            print(form.errors)

    form = CourseForm()
    context = {
        "form": form
    }
    return render(request, 'add_course.html', context)




